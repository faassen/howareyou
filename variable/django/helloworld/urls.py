from django.conf.urls import url
from helloworld.views import welcome

urlpatterns = [
    url(r'^users/(?P<name>\w+)$', welcome, name='welcome')
]
