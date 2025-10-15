from django.shortcuts import render
from django.views.generic import View, ListView
from projects.models import Project
from tasks.models import Task
from accounts.models import Profile
# from notifications.models import Notification
from teams.models import Team
# from django.contrib.auth.mixins import LoginRequiredMixin

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
        

        # print("Memebers : ", latest_members)
        context = {}
        # if request.user.is_authenticated:
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
        context['title'] = "Dashboard"
        return render(request, "accounts/dashboard.html", context)
    

class MemberListView(ListView):
    model = Profile
    context_object_name = "members"
    template_name = "project/profile_list.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # latest notifications
        context = super(MemberListView, self).get_context_data(**kwargs)
        latest_notification = self.request.user.notifications.unread()
        context['notification_count'] = latest_notification.count()
        context['latest_notification'] = latest_notification[:3]
        context['header_text'] = "Member"
        context['title'] = "All Members"
        return context
    

