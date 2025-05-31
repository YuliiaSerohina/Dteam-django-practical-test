from django.db import models


class CV(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    skills = models.TextField(help_text="List your skills separated by commas", blank=True)
    projects = models.TextField(help_text="Describe your projects", blank=True)
    contacts = models.TextField(help_text="Provide your contact information", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.contacts} {self.bio} {self.skills} {self.projects}"

