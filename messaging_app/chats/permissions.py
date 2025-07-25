from rest_framework import permissions
from .models import Message


class IsOwnerOrParticipant(permissions.BasePermission):
    """
    Custom permission to allow only participants of a conversation
    to send, view, update, or delete messages.
    """

    def has_object_permission(self, request, view, obj):
        # obj can be a Message or a Conversation
        user = request.user

        if isinstance(obj, Message):
            return user in obj.conversation.participants.all()
        
        # Fallback if obj is a Conversation
        return user in obj.participants.all()
