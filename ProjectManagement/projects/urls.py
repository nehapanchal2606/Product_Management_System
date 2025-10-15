from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='list'),
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('near-due-date/', views.ProjectNearDueDateListView.as_view(), name='due-list'),
]