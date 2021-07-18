from rest_framework import serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','bio','profile_pic','contact']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['user','title','project_image','project_description','link']
