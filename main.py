import time
import json
import random
import yaml
from ConfigLoader import ConfigLoader
from SchemaBuilder import SchemaBuilder
from MessageGenerator import MessageGenerator
from SchemaLoader import SchemaLoader

def main():
    # Create an instance of ConfigLoader to load the configuration from a YAML file
    config_loader = ConfigLoader("config.yaml")
    # Load the schema definition from the configuration
    schema_definition = config_loader.get_schema_definition()
    schema_loader = SchemaLoader(schema_definition)
    schema_builder = schema_loader.build_schema()
    
    # Create an instance of MessageGenerator with the generator definition and the SchemaBuilder
    generator_definition = config_loader.get_generator_definition()
    generator = MessageGenerator(generator_definition, schema_builder)
    
    generator.run()


if __name__ == "__main__":
    main()

