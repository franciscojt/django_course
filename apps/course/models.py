from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s the Courses" % self.name

class Descriptions(models.Model):
    content = models.TextField(null=True)
    course_id = models.OneToOneField(Courses, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s the description" % self.course_id.name

class Comments(models.Model):
    content = models.TextField(null=True)
    course_id = models.ForeignKey(Courses)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s the comments" % self.course_id.name
