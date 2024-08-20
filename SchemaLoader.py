import yaml
from SchemaBuilder import SchemaBuilder

# Initialize SchemaLoader with the schema definition (a dictionary)
class SchemaLoader:
    def __init__(self, schema_definition):
        self.schema = schema_definition

    def build_schema(self):
        return SchemaBuilder(self.schema)
