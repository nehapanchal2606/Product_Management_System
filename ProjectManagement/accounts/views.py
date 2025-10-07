from django.shortcuts import render
from django.views.generic import View
from projects.models import Project
from tasks.models import Task
from accounts.models import Profile
# from notifications.models import Notification
from teams.models import Team

# Create your views here.

# class DashboardView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "accounts/dashboard.html")
    

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        latest_project = Project.objects.all()
        latest_tasks = Task.objects.all()
        latest_members = Profile.objects.all()
        latest_teams = Team.objects.all()
        

        print("Memebers : ", latest_members)
        context = {}
        if request.user.is_authenticated:
            latest_notification = request.user.notifications.unread()
            context['notification_count'] = latest_notification.count()
            context['latest_notification'] = latest_notification[:3]
            
        context['latest_project'] = latest_project[:5]
        context['latest_project_count'] = latest_project.count()
        context['projects_near_due_date'] = latest_project.due_in_two_days_or_less()[:5]
        # context['latest_tasks_count'] = latest_tasks.count()
        context['latest_members'] = latest_members
        context['latest_members_count'] = latest_members.count()
        context['team_count'] = latest_teams.count()
        context['header_text'] = "Dashboard"
        return render(request, "accounts/dashboard.html", context)
    

