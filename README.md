
## Random Number Generator API

![gif](https://miro.medium.com/max/1400/1*YOVHPHgA64ET719WTw0pvw.gif)


# Description

Provide an API which generates a random no for a given URL.
The random no must be saved in the redis NoSQL database.
If the same URL is sent again, don't generate a new number, instead return the one previously generated and saved in Redis.
Every time the random no is generated, push that number as a message to kafka.
Kafka consumers should read the number and save it in the file with URL mapping.


e.g.

User makes an API call with youtube.com, the API returns a random number say 10023.
User makes an API call with liverpoolfc.com API returns a random number say 98345.
User again makes an API call with youtube.com and the server returns 10023 previously returned in step 1
Kafka consumer saves following mapping in the file
youtube.com 10023 liverpoolfc.com 98345

Please ensure to use Django for the API server, api will push msg in kafka, and in the dataprocessor that msg will be consumed and processed.


## Requirements

Last tested successfully with Python 3.6.13 and Ubuntu 16.04

Create venv and pip install django to import the required modules.


## Technologies used

[Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).

[DRF](https://github.com/gitgik/django-rest-api/blob/master/www.django-rest-framework.org): A powerful and flexible toolkit for building Web APIs


## Quick Setup

1. Create a folder for your project on your local machine
```bash
  mkdir random_number_generator_api; 
  cd random_number_generator_api

```

2. Create a virtual environment and install django

```bash
  virtualenv --python=python3 venv_random_number_generator_api; 
  source venv_random_number_generator_api/bin/activate; 

```

Install the dependencies needed to run the app:
```bash
  pip install Django==3.2.13
  pip install -r requirements. txt 

```

3. Download this project template from GitHub
```bash
  git clone https://github.com/parshurampatil197/random_number_generator_api.git; 
  cd random_number_generator_api

```

4. Initialize the database

```bash
  python manage.py makemigrations
  python manage.py migrate

```


5. Install Apache Kafka on Ubuntu 16.04 [here](https://tecadmin.net/install-apache-kafka-ubuntu/)

    1)Start Kafka Server
```bash
  sudo systemctl start zookeeper
  sudo systemctl start kafka
  sudo systemctl status kafka

```

    2)Create a Topic in Kafka

```bash
parshuram@parshuram:~$ kafka_2.13-3.0.0/bin/kafka-topics.sh --create --topic random_num_gen --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 

parshuram@parshuram:~$ kafka_2.13-3.0.0/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
random_num_gen

```

Kafka also has a command-line consumer to read data from the Kafka cluster and display messages to standard output.
```bash
  parshuram@parshuram:~$  kafka_2.13-3.0.0/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic random_num_gen --from-beginning

```


6. Install redis on Ubuntu 16.04 [here](https://askubuntu.com/questions/868848/how-to-install-redis-on-ubuntu-16-04)
    
    1)Start redis service:
```bash
  sudo systemctl start redis
  systemctl status redis

```
2)Test instance:
```bash
parshuram@parshuram:~$ redis-cli
127.0.0.1:6379> CONFIG SET requirepass "root"
OK
127.0.0.1:6379> AUTH root
OK
127.0.0.1:6379> ping
PONG

```


Run the project

```bash
  python manage.py runserver

```











## API Reference
 
API Testing done by POSTMAN
#### Http request: POST 

```http
  http://127.0.0.1:8000/v1/users/random-num-gen
```

#### Request

```http
  {
    "url":"https://instgram.com"
}
```
#### Response

```http
{
    "url": "instgram.com",
    "random_number": 26430
}
```


## Authors

- [@parshuram](https://github.com/parshurampatil197)
