from django.shortcuts import render
from .models import Project,Profile
# Create your views here.

def index(request):
    all_projects = Project.all_projects()
    return render(request,'index.html',{"all_projects":all_projects})

def profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user)
    projects = Project.objects.filter(user=user)
    return render(request,'profile.html',{"user":user,"profile":profile,"projects":projects})
