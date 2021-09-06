from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('snack_detail',args=[str(self.id)])
