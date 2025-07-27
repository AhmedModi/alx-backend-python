from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role']


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'sender_username', 'content', 'timestamp']

    def get_sender_username(self, obj):
        return obj.sender.username


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    topic = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'messages', 'topic']

    def validate_topic(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Topic must be at least 3 characters long.")
        return value
