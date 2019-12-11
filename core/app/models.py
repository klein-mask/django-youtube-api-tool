from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    class Meta:
        db_table = 'videos'

    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title