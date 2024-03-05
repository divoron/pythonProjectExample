from django.db import models
from django.utils import timezone


# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    for_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    status = models.BooleanField(default=None)
    priority = models.CharField(max_length=10)

    def __str__(self):
        return self.description
