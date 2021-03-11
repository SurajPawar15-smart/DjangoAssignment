from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendbt, name='back'),
    path('send/', views.send, name="send")
]
