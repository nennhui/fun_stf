from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.index, name='index'),
url(r'^touch/', views.touch, name='touch'),
url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]