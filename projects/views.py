from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from .models import Project

class ProjectsView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(request, 'projects/display.html', context)
