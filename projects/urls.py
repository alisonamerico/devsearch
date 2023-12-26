from django.urls import path

from projects.views import project, projects

urlpatterns = [
    path('projects/', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
]
