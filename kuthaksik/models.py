from django.db import models
from datetime import datetime

# Create your models here.

class Haksik(models.Model):
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()
    created_at = models.DateTimeField(verbose_name='created at')
    updated_at = models.DateTimeField(verbose_name='updated at')

    def save(self, *args, **kwargs):
        if not self.id:  # Object is a new instance
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.updated_at = datetime.now()
        return super(Haksik, self).save(*args, **kwargs)