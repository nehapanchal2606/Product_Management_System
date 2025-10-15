from django.urls import path
from notifications import views

app_name = "notifications"

urlpatterns = [
    path('notification-list/', views.NotificationListView.as_view(), name="notification-list")
]