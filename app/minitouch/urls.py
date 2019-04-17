from . import views
from django.conf.urls import url
urlpatterns = [
url(r'^touch/', views.touch, name='touch'),
]