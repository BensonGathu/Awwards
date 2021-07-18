from django.shortcuts import render,redirect
from .models import Project,Profile
from .forms import ProfileForm,ProjectForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer


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

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def index(request):
    all_projects = Project.all_projects()
    return render(request,'index.html',{"all_projects":all_projects})

@login_required(login_url="login")
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            redirect(request.path_info)
    else:
        form = ProfileForm(instance=request.user.profile)
    profile = Profile.objects.filter(user=user)
    projects = Project.objects.filter(user=user)
    return render(request,'profile.html',{"user":user,"profile":profile,"projects":projects,"form":form})

@login_required(login_url="login")
def search(request):
    if 'projectname' in request.GET and request.GET['projectname']:
        searchproject = request.GET.get('projectname')
        result_projects = Project.search_project(searchproject)
        message = f'{searchproject}'

        return render(request,"searchresults.html",{"message":message,"result_projects":result_projects})

    else:
        message = "Search for a project"
        return render(render,"searchresults.html",{"message":message})

@login_required(login_url="login")
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

@login_required(login_url="login")
def singleproject(request,id):
    project = Project.objects.get(id=id)

    return render(request,'project.html',{"project":project})

class ProjectDet(APIView):
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)

class Profiles(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)