from django.db import models

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    pictures = models.ImageField(upload_to='pictures/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name