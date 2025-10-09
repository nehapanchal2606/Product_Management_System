from django.shortcuts import render, redirect
from projects.models import Project
from django.views.generic import CreateView, ListView
from projects.forms import ProjectForm
from django.urls import reverse_lazy

from notifications.tasks import create_notification
from django.contrib.contenttypes.models import ContentType

# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_create.html"
    success_url = reverse_lazy("accounts:dashboard")

    def form_valid(self, form):
        project = form.save(commit=False)
        project.owner = self.request.user
        project.save()

        # send notification 
        actor_username = self.request.user.username
        verb = f"New Project Assignment, {project.name}"
        object_id = project.id

        create_notification.delay(
            actor_username=actor_username, 
            verb=verb,
            object_id=object_id)

        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        # latest notifications
        if self.request.user.is_authenticated:
            latest_notification = self.request.user.notifications.unread()
            context = super(ProjectCreateView, self).get_context_data(**kwargs)
            context['notification_count'] = latest_notification.count()
            context['latest_notification'] = latest_notification[:3]
        context['header_text'] = "Dashboard"
        return context


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = 'project/project_list.html'
    paginate_by = 2


