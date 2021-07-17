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

def search(request):
    if 'projectname' in request.GET and request.GET['projectname']:
        searchproject = request.GET.get('projectname')
        result_projects = Project.search_project(searchproject)
        message = f'{searchproject}'

        return render(request,"searchresults.html",{"message":message,"result_projects":result_projects})

    else:
        message = "Search for a project"
        return render(render,"searchresults.html",{"message":message})

