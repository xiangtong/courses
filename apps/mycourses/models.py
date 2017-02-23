from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    # desc = models.CharField(max_length=50)
    # desc=models.OneToOneField(Desc)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Desc(models.Model):
    desc=models.TextField(default='this is desc')
    course=models.OneToOneField(Course,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
