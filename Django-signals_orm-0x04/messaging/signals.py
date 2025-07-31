from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Messages where the user was sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Notifications and message history (already cascaded by FK if defined correctly)
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(message__sender=instance).delete()

@receiver(pre_save, sender=Message)
def log_message_edits(sender, instance, **kwargs):
    if not instance.pk:
        return  # It's a new message, not an edit

    try:
        old_message = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return

    if old_message.content != instance.content:
        # Log the old content
        MessageHistory.objects.create(
            message=instance,
            old_content=old_message.content
        )
        instance.edited = True
