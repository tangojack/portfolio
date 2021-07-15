from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from .models import Project

class ProjectView(View):

    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)
        context = {
            'project': project
        }
        return render(request, 'projects/display.html', context)
