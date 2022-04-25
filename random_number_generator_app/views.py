import json
import redis
import random
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from kafka import KafkaProducer,KafkaConsumer
from tldextract import extract

redis_instance = redis.Redis(host='localhost', port=6379, db=0, password='root')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
# consumer = KafkaConsumer('testTopic',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',
# enable_auto_commit=True,group_id='my-group',value_deserializer=lambda x: json.loads(x.decode('utf-8')))



class UserViewSet(ModelViewSet):
        def __init__(self, **kwargs):
                super().__init__(**kwargs)

        @action(methods=['post'], detail=False, url_path='random-num-gen')
        def random_num_gen(self, request, *args, **kwargs):
                url = extract(request.data['url']).registered_domain
                random_num = redis_instance.get(url)
                if not random_num:
                        random_num = random.randint(10000,99999)
                        random_num = json.dumps(random_num)
                        redis_instance.set(url,random_num)
                random_num = json.loads(random_num)
                data = {"url": url, "random_number": random_num}
                producer.send("testTopic", json.dumps(data).encode('utf-8'))
                return Response(data = data)