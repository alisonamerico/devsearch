from django.shortcuts import render
from projects.forms import ProjectForm

from projects.models import Project

def projects(request):
    projects_obj = Project.objects.all()
    context = {'projects': projects_obj}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(
        request, 'projects/single-project.html', {'project': project_obj}
    )

def create_project(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'project_form.html', context)    
