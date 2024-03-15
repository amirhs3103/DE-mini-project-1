import json 
from kafka import KafkaConsumer, KafkaProducer
from datetime import datetime

consumer = KafkaConsumer(
    'topic1',
     bootstrap_servers=['localhost:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9094'], max_block_ms=5000)

for message in consumer:
 message.value['time_stamp'] = str(datetime.today())
 producer.send('topic2', json.dumps(message.value).encode('utf-8'))