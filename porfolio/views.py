from django.shortcuts import render
from .models import Project


def portafolio(request):
    projects = Project.objects.all()

    return render(request,'porfolio/portafolio.html', {'projects':projects})
# Create your views here.
