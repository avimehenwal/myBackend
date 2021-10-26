import json
from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project
from django.http import JsonResponse
from django.core import serializers


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def project_json(request):
    project = list(Project.objects.values())
    return JsonResponse({'data': project})
