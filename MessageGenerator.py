import time
import yaml


class MessageGenerator:
    # Initialize MessageGenerator with the generator definition and a SchemaBuilder
    def __init__(self, generator_definition, schema_builder):
        self.interval = generator_definition.get("frequency")
        self.schema_builder = schema_builder
        self.destination_type = generator_definition.get("destination", {}).get("type", "console")

    def run(self):
        while True:
            message = self.schema_builder.create_message()

            self.send_message(message)

            time.sleep(self.interval)

    def send_message(self, message):
        if self.destination_type == "console":
            print(message)
        else:
            raise ValueError(f"Destination type '{self.destination_type}' not supported.")
