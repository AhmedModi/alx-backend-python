from rest_framework import viewsets, status, filters, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsOwnerOrParticipant, IsParticipantOfConversation


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrParticipant]
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__username']

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['timestamp']

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get('conversation')
        if self.request.user not in conversation.participants.all():
            raise serializers.ValidationError("You are not a participant of this conversation.")
        serializer.save(sender=self.request.user)
