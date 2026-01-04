from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    log_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.message}"
