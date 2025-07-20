from django.urls import path
from .views import MessageListCreateAPIView

urlpatterns = [
    path('messages/', MessageListCreateAPIView.as_view(), name='message_list_create')
]
