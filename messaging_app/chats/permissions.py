# messaging_app/chats/permissions.py

from rest_framework import permissions

class IsOwnerOrParticipant(permissions.BasePermission):
    """
    Custom permission to only allow users to access their own messages or conversations.
    """

    def has_object_permission(self, request, view, obj):
        # For messages: obj.sender or obj.receiver
        # For conversations: obj.participants (assumed to be a many-to-many field)
        return request.user == obj.sender or request.user == obj.receiver or request.user in obj.participants.all()
