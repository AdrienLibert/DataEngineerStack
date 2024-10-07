import random
from datetime import datetime

class SchemaBuilder:
    def __init__(self, schema_definition):
        self.schema = schema_definition

    def create_message(self):
        message = {}
        for field, type_config in self.schema.items():
            if type_config['type'] == 'integer':
                message[field] = random.randint(type_config['min'], type_config['max'])
            elif type_config['type'] == 'string':
                message[field] = random.choice(type_config['values'])
            elif type_config['type'] == 'float':
                message[field] = round(random.uniform(type_config['min'], type_config['max']), 2)
            elif type_config['type'] == 'datetime':
                message[field] = datetime.now().strftime(type_config['format'])
        return message
