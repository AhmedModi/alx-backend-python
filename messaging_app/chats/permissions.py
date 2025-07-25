from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow access only to authenticated users who are participants of the conversation.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:  # <-- Required line
            return False

        if request.method in ['GET', 'POST']:
            return request.user in obj.conversation.participants.all()

        if request.method in ['PUT', 'PATCH', 'DELETE']:  # <-- Required line
            return request.user in obj.conversation.participants.all()

        return False
