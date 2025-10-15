from django.shortcuts import render
from django.views.generic import ListView
from notifications.models import Notification
# Create your views here.


class NotificationListView(ListView):
    model = Notification
    context_object_name = "notifications"
    template_name = "notification/notification_list.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # latest notifications
        context = super(NotificationListView, self).get_context_data(**kwargs)
        latest_notification = self.request.user.notifications.unread()
        context['notification_count'] = latest_notification.count()
        context['latest_notification'] = latest_notification[:3]
        context['header_text'] = "Projects"
        context['title'] = "All Notification"

        return context