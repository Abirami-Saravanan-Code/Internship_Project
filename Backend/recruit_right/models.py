from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('hiring_manager', 'Hiring Manager'),
        ('sourcing_team', 'Sourcing Team'),
        ('interviewer', 'Interviewer'),
        ('candidate', 'Candidate'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='candidate')

    def __str__(self):
        return f"{self.name} ({self.role})"


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to User model
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()

    def __str__(self):
        return self.user.name
