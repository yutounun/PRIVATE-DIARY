from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    """diary model"""

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True, null=True)
    photo1 = models.ImageField(blank=True, null=True)
    photo2 = models.ImageField(blank=True, null=True)
    photo3 = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
