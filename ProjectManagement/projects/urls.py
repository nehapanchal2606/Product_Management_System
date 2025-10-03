from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('create/', views.ProjectCreateView.as_view(), name='create'),
]