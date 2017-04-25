from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length = 50)
    created_at = models.DateField(auto_now = True)

class Description(models.Model):
    course = models.OneToOneField(
        Courses,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    description = models.CharField(max_length = 100)
class Comments(models.Model):
    course = models.ForeignKey(Courses)
    comment = models.TextField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
