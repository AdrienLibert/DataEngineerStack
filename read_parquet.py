from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ReadParquet") \
    .getOrCreate()

df_parquet = spark.read.parquet("./parquet_output")

df_parquet.show(truncate=False)

df_parquet.printSchema()
