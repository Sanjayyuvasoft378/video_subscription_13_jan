from django.db import models

# Create your models here.
from membership.models import Membership

class Courses(models.Model):
    slugg = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_membership = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    tumbnail = models.ImageField()
    def __str__(self):
        return self.title

