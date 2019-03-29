from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
<<<<<<< HEAD
    uuser = models.OneToOneField(User, on_delete=models.CASCADE,
        blank=True, null=True)
=======
    user = models.OneToOneField(User, blank=True, null=True)
>>>>>>> e84bbae6cde2ae14b5dacaaf73ce989ce78e70f8
