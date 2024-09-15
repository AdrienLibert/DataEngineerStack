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
