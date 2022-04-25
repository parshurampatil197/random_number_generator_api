# from rest_framework import status
# from rest_framework.response import Response
# from ..serializers.user_serializers import UrlSerializer


from django.test import TestCase, Client
from http.cookies import SimpleCookie
from ..models.user_models import User
import json


class UrlTestCase(TestCase):

    @classmethod
    def setUp(self):
        self.url = 'https://google1.com'
        self.client = Client()
        self.cookie = {'_ia_jwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDA0MDE5MjEtNmYzNi00MjkyLWI0NjItMWIyZTA3OGYzY2VhIiwidXNlcm5hbWUiOiJ0ZXN0X3VzZXIyQGdtYWlsLmNvbSIsImV4cCI6MTY1NzUzNDIyMSwiZW1haWwiOiJ0ZXN0X3VzZXIyQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjQxOTgyMjIxfQ.bli3cXFpViJ_nMpAXpe_vvZHinw7y2m4yoyxIn4aEns'}
        self.user, created = User.objects.get_or_create(email='test_user2@gmail.com')

    def test_url_validation(self):
        url_path = "/v1/users/random-num-gen"
        self.client.cookies = SimpleCookie(self.cookie)
        response = self.client.post(path=url_path, data={'url': self.url}, content_type='application/json')
        response_dict = json.loads(response.content)

        self.assertEqual(response_dict['status']['status_code'], 1001)





    # def test_url_validation(self):
    #     data = {'URL': self.url}
    #     serializer = UrlSerializer(data=data)
    #     if serializer.is_valid():
    #         response1 = Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         response1 = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response1.status_code, 200)
