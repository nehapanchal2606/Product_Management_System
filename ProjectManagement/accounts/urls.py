from django.urls import path
from .views import DashboardView, MemberListView

app_name = 'accounts'

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("members/", MemberListView.as_view(), name="members-list"),
]
