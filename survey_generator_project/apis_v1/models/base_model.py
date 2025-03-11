from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_%(class)ss')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_%(class)ss')

    class Meta:
        abstract = True
