from django.urls import path
from . import views

urlpatterns = [
    path('save_msg', views.save_msg, name="save_msg_endpoint")
]
