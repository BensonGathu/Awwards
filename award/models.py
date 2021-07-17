from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='name')
    profile_pic = models.ImageField(upload_to='images/',default='SOME IMAGE')
    bio = models.CharField(max_length=250)
    contact = models.IntegerField()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls,username):
        return cls.objects.fiter(user__username__icontains = username).all()



class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    project_image = models.ImageField(upload_to='images/')
    project_description = models.TextField(max_length=255)
    link = models.URLField(max_length=250)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def search_project(cls,seach_name):
        return cls.objects.filter(title__icontains=search_name).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.order_by("-id")
