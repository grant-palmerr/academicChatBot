# professors/models.py
from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=100)
    research_area = models.CharField(max_length=500)
    publications = models.TextField()
    education = models.TextField()
    teaching_area = models.TextField()

    def __str__(self):
        return self.name