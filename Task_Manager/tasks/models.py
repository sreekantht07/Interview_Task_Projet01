from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
