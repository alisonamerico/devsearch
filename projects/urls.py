from django.urls import path

from projects.views import project, projects, create_project

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', create_project, name='create-project'),
]
