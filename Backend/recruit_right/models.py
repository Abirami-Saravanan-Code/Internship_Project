# Create your models here.
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()

    def __str__(self):
        return self.name
