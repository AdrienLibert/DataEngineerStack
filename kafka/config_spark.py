class KafkaConfig:
    def __init__(self, bootstrap_servers="localhost:9092", topic="orders", starting_offsets="earliest"):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.starting_offsets = starting_offsets

class ETLConfig:
    def __init__(self, parquet_output="./parquet_output", checkpoint_path="./checkpoint"):
        self.parquet_output = parquet_output
        self.checkpoint_path = checkpoint_path