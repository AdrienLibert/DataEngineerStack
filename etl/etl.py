from kafka.spark_utils import create_spark_session, read_from_kafka, parse_json, aggregate_avg_price, write_to_console
from kafka.config_spark import KafkaConfig, ETLConfig
from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType

def main():
    kafka_config = KafkaConfig()
    etl_config = ETLConfig()

    spark = create_spark_session(app_name="KafkaSparkStreaming")

    df_kafka = read_from_kafka(spark, kafka_config.bootstrap_servers, kafka_config.topic)
    
    # Define schema for JSON data
    schema = StructType([
        StructField("order_id", StringType(), True),
        StructField("symbol", StringType(), True),
        StructField("order_type", StringType(), True),
        StructField("quantity", FloatType(), True),
        StructField("price", FloatType(), True),
        StructField("timestamp", TimestampType(), True)
    ])

    df_parsed = parse_json(df_kafka, schema)
    df_avg_price = aggregate_avg_price(df_parsed)

    # query = write_to_parquet(df_avg_price, etl_config.output_path, etl_config.checkpoint_path)
    query = write_to_console(df_avg_price)
    query.awaitTermination()

if __name__ == "__main__":
    main()
