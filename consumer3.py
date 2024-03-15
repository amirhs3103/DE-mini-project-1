import json 
from kafka import KafkaConsumer
import psycopg2

consumer = KafkaConsumer(
    'topic3',
     bootstrap_servers=['localhost:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

conn = psycopg2.connect(
    dbname="miniproject_db",
    user="postgres",
    password=1234,
    host="localhost",
    port="5432"
)
cur = conn.cursor()

for message in consumer:

    cur.execute(
    "INSERT INTO users (id, first_name, last_name, gender, address, post_code, email, username, dob, registered_date, phone, picture, time_stamp, cat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (message.value['id'], message.value['first_name'], message.value['last_name'], message.value['gender'], message.value['address'], message.value['post_code'], message.value['email'], message.value['username'], message.value['dob'], message.value['registered_date'], message.value['phone'], message.value['picture'], message.value['time_stamp'], message.value['cat'])
    )   

    conn.commit()


cur.close()
conn.close()
