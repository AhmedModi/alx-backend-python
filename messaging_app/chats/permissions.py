from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Conversation

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to only allow participants of a conversation
    to view, send, update, or delete messages.
    """

    def has_permission(self, request, view):
        # Must be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        obj can be a Conversation or Message instance.
        We check if the user is a participant in the conversation.
        """
        if hasattr(obj, 'participants'):
            # Direct Conversation object
            return request.user in obj.participants.all()
        elif hasattr(obj, 'conversation'):
            # Message object: check conversation participants
            return request.user in obj.conversation.participants.all()
        return False
