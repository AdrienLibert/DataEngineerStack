from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg, window
from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType

# Create Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2") \
    .getOrCreate()

# Read from Kafka topic 'orders'
df_kafka = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert Kafka messages from binary to string
df_kafka = df_kafka.selectExpr("CAST(value AS STRING) as value")

# Define schema for JSON data
schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("symbol", StringType(), True),
    StructField("order_type", StringType(), True),
    StructField("quantity", FloatType(), True),
    StructField("price", FloatType(), True),
    StructField("timestamp", TimestampType(), True)
])

# Parse JSON and extract fields
df_parsed = df_kafka.withColumn("data", from_json(col("value"), schema)).select("data.*")

df_with_watermark = df_parsed.withWatermark("timestamp", "5 minutes")

# Calculate average price over 5-minute per symbol
df_avg_price = df_with_watermark \
    .groupBy(window(col("timestamp"), "5 minutes"), col("symbol")) \
    .agg(avg(col("price")).alias("avg_price")) \
    .filter(col("avg_price").isNotNull())  # Filter out null average prices

# Write results to Parquet files
query = df_avg_price.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "./parquet_output") \
    .option("checkpointLocation", "./checkpoint") \
    .start()

# Keep the stream running
query.awaitTermination()
