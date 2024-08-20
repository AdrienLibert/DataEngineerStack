import random


class SchemaBuilder:
    def __init__(self, schema_definition):
        self.schema = schema_definition

    def create_message(self):
        # Retrieve the list of messages from the schema definition
        messages = self.schema.get("messages", [])
        
        if not messages:
            raise ValueError("La clé 'messages' est absente ou la liste est vide dans le schéma.")
        
        return random.choice(messages)
