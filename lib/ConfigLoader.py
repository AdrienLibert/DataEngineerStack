import yaml

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_config()

    # Open the configuration file and load its content as a dictionary
    def load_config(self):
        with open(self.config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def get_generator_definition(self):
        # Retrieve the "generator" section from the configuration file, or an empty dictionary if it doesn't exist
        return self.config.get("generator", {})

    def get_schema_definition(self):
        # Retrieve the "schema" section from the configuration file, or an empty dictionary if it doesn't exist
        return self.config.get("schema", {})


class KafkaConfig:
    def __init__(self, bootstrap_servers="localhost:9092", topic="orders", starting_offsets="earliest"):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.starting_offsets = starting_offsets


class ETLConfig:
    def __init__(self, parquet_output="./parquet_output", checkpoint_path="./checkpoint"):
        self.parquet_output = parquet_output
        self.checkpoint_path = checkpoint_path
