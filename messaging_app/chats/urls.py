from django.urls import path
from .views import MessageListCreateAPIView
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = router.urls

urlpatterns = [
    path('messages/', MessageListCreateAPIView.as_view(), name='message_list_create')
]
