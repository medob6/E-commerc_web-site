from django.urls import path
from . import views

urlpatterns = [
    path('store/hello/', views.say_hello, name = 'hello'),
]