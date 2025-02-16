# Generated by Django 5.1.5 on 2025-02-03 01:25

from django.db import migrations
from django.contrib.auth.models import Group

# Function to create the roles (groups)
def create_roles(apps, schema_editor):
    roles = ['Admin', 'Hiring Manager', 'Sourcing Team', 'Interviewer', 'Candidate']
    for role in roles:
        Group.objects.get_or_create(name=role)

class Migration(migrations.Migration):

    dependencies = [
        ('recruit_right', '0001_initial'),  # Replace 'previous_migration_name' with the latest migration
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]

