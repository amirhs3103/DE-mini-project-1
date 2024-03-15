you can install the requirments of this project with poetry in python

when you run docker compose up in the main directory following services will start:
kafka
zookeeper
postgres
producer: its an ubuntu image with python and required packages installed which will be built with Dockerfile-ubuntu in the main directory

then you can set up a cron job task to run the producer.py file in the codes directory which is /home/codes/producer.py in the producer container and run in with python3 to produce data and send in to topic1 in kafka

you can set up full backup + wal archiving in postgres

you can run consumer1.py to get data from topic1 and add a time_stamp column to it and send it to topic2 in kafka

you can run consumer2.py to get data from topic2 and add a random cat column to it and send it to topic3 in kafka

you can run consumer3.py to get data from topic3 and send in to postgres database in users table