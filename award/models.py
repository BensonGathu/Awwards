from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='name')
    profile_pic = models.ImageField(upload_to='images/',default='SOME IMAGE')
    bio = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.user.username

    def save(self):
        self.save()


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    project_image = models.ImageField(upload_to='images/')
    project_description = models.TextField()
    link = models.URLField(max_length=250)

    def __str__(self):
        return self.title

    def save(self):
        self.save()

