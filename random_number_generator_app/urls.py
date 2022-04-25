from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter(trailing_slash=False)

router.register('users', UserViewSet,basename='user')
urlpatterns = router.urls
