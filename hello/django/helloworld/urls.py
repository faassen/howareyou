from django.conf.urls import url
from helloworld.views import welcome

urlpatterns = [
    url(r'^welcome$', welcome, name='welcome')
]
