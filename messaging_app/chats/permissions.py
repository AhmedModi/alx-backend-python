from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        # Determine the conversation object
        if hasattr(obj, 'conversation'):
            conversation = obj.conversation
        else:
            conversation = obj  # If the object is already a Conversation

        # Only allow if user is a participant
        if request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user in conversation.participants.all()

        return False
