from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2") \
    .getOrCreate()

df_kafka = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders") \
    .option("startingOffsets", "earliest") \
    .load()

df_kafka = df_kafka.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

query = df_kafka.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
