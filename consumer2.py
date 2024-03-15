import json 
from kafka import KafkaConsumer, KafkaProducer
from random import choice

consumer = KafkaConsumer(
    'topic2',
     bootstrap_servers=['localhost:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9094'], max_block_ms=5000)

cats = ['A', 'B', 'C', 'D']
for message in consumer:
 message.value['cat'] = choice(cats)
 producer.send('topic3', json.dumps(message.value).encode('utf-8'))