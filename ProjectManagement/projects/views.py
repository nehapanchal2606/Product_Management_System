from django.shortcuts import render
from projects.models import Project
from django.views.generic import CreateView
from projects.forms import ProjectForm
from django.urls import reverse_lazy
# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_create.html"
    success_url = reverse_lazy("accounts:dashboard")




