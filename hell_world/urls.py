from django.urls import path
from hell_world import views

urlpatterns = [
    path('', views.hell_world, name='hell_world'),
]