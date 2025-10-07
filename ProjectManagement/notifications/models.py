from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class NotificationManager(models.Manager):
    # def for_user(self,user):
    #     return self.filter(receipient=user)
    
    def unread(self):
        return self.filter(read=False)
    
    def read(self):
        return self.filter(read=True)


class Notification(models.Model):
    receipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actions")
    verb = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=36)
    content_object = GenericForeignKey('content_type', 'object_id')
    create_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    objects = NotificationManager()

    def __str__(self):
        return f'{self.actor} {self.verb} {self.content_object}'
    
    class Meta:
        ordering = ['-create_at']

    @property
    def notification_time_formatted(self):
        return self.create_at.strftime('%d %b %I:%M %p')


