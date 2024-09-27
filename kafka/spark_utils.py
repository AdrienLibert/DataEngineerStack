from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg, window
from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType


# Create Spark session
def create_spark_session(app_name="SparkApplication", kafka_version="org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2"):
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.jars.packages", kafka_version) \
        .getOrCreate()


# Read from Kafka topic and return DF
def read_from_kafka(spark, kafka_bootstrap_servers, topic, starting_offsets="earliest"):
    df_kafka = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
        .option("subscribe", topic) \
        .option("startingOffsets", starting_offsets) \
        .load()
    return df_kafka.selectExpr("CAST(value AS STRING) as value")

# Parse JSON and extract fields
def parse_json(df_kafka, schema):
    return df_kafka.withColumn("data", from_json(col("value"), schema)).select("data.*")


# Calculate average price over 5-minute per symbol
def aggregate_avg_price(df, time_window="5 minutes"):
    return df.withWatermark("timestamp", "5 minutes") \
             .groupBy(window(col("timestamp"), time_window), col("symbol")) \
             .agg(avg(col("price")).alias("avg_price")) \
             .filter(col("avg_price").isNotNull())

# Write results to Parquet files
def write_to_parquet(df, output_path, checkpoint_path):
    return df.writeStream \
        .outputMode("append") \
        .format("parquet") \
        .option("path", output_path) \
        .option("checkpointLocation", checkpoint_path) \
        .start()

# Write results to console
def write_to_console(df):
    return df.writeStream \
        .outputMode("append") \
        .format("console") \
        .option("truncate", "false") \
        .start()

# Read from Parquet files
def read_from_parquet(spark, input_path):
    return spark.read.parquet(input_path)