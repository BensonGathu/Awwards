from django.shortcuts import render,redirect
from .models import Project,Profile
from .forms import ProfileForm,ProjectForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
           
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'registration/register.html',{"form":form})

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

def uploadproject(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST or None,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('index')
    else:
        form = ProjectForm()
    return render(request,'projectform.html',{"form":form})

