import time
from ConfigLoader import ConfigLoader
from SchemaBuilder import SchemaBuilder
from MessageGenerator import MessageGenerator

def main():
    config_loader = ConfigLoader("config.yaml")
    schema_definition = config_loader.get_schema_definition()
    schema_builder = SchemaBuilder(schema_definition)
    
    generator_definition = config_loader.get_generator_definition()
    generator = MessageGenerator(generator_definition, schema_builder)
    
    generator.run()

if __name__ == "__main__":
    main()


