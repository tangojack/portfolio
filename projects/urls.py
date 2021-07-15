from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('<int:project_id>/', views.ProjectView.as_view(), name="project"),
]
