from celery import shared_task
from django.utils import timezone
from notifications.models import Notification
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


@shared_task
def create_notification(actor_username, verb, object_id):
    try:
        actor = User.objects.get(username=actor_username)
        content_type = ContentType.objects.get_for_model(Project)
        content_object = Project.objects.get(id=object_id)

        project = Project.objects.get(id=object_id)

        # get all team member
        members = project.team.members.all()

        for member in members:
            notification = Notification.objects.create(
                receipient=member,
                actor=actor,
                verb=verb,
                content_type=content_type, 
                content_object=content_object,
                read=False
            )

        return notification.verb

    except User.DoesNotExist:
        return None
    except ContentType.DoesNotExist:
        return None
