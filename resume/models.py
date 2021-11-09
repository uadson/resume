from django.db import models

# Timezone
from django.utils import timezone

# Custom User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Main(models.Model):
    create = models.DateField("Create", default=timezone.now)
    modified = models.DateField("Modified", default=timezone.now)
    active = models.BooleanField("Active", default=True)

    class Meta:
        abstract = True


class Project(Main):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description", blank=True)
    responsabilities = models.TextField("Responsabilities", blank=True)
    tools = models.TextField("Tools", blank=True)
    github_url = models.URLField("Github", max_length=200, blank=True)
    url = models.URLField("Page", max_length=200, blank=True)

    def __str__(self):
        return self.title
