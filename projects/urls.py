from django.urls import path

from projects.views import create_project, delete_project, project, projects, update_project

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', create_project, name='create-project'),
    path('update-project/<str:pk>/', update_project, name='update-project'),
    path('delete-project/<str:pk>/', delete_project, name='delete-project'),
]
