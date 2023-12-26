from django.shortcuts import HttpResponse


def projects(request):
    return HttpResponse('Here are our projects')


def project(request, pk):
    return HttpResponse(f'SINGLE PROJECT {pk}')
