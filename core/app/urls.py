from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('index/', views.index, name='app_index'),
    path('video/', views.video, name='app_video'),
    path('channel/', views.channel, name='app_channel'),
    path('channel/sort/', views.channel, name='video_sort'),
]