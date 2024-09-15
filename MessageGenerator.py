from confluent_kafka import Producer
import json
import time

class MessageGenerator:
    def __init__(self, generator_definition, schema_builder):
        self.interval = generator_definition.get("frequency", 1)
        self.schema_builder = schema_builder
        self.destination_type = generator_definition.get("destination", {}).get("type", "console")
        self.kafka_producer = None
        
        if self.destination_type == "kafka": #Initialisation
            self.kafka_producer = Producer({
                'bootstrap.servers': 'localhost:9092'
            })

            self.kafka_topic = generator_definition.get("destination", {}).get("topic", "default_topic")  #destination

    def run(self):
        while True:
            message = self.schema_builder.create_message()
            self.send_message(message)
            self.kafka_producer.poll(0)#callback
            time.sleep(self.interval)

    def send_message(self, message):
        if self.destination_type == "console":
            print(message)
        elif self.destination_type == "kafka":
            self.kafka_producer.produce(
                self.kafka_topic, 
                key=None, 
                value=json.dumps(message).encode('utf-8'),
                callback=self.delivery_report #to verify if the message was sent
            )
            self.kafka_producer.flush()#to send messages
            print(f"Message sent to orders '{self.kafka_topic}': {message}")
        else:
            raise ValueError(f"Destination type '{self.destination_type}' not supported.")

    @staticmethod
    def delivery_report(err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")