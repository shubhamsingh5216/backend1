# designers/models.py
from django.db import models
class Designer(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.TextField()
    projects = models.IntegerField()
    years = models.IntegerField()
    price = models.CharField(max_length=10)
    shortlisted = models.BooleanField(default=False)  # <-- NEW

    def __str__(self):
        return self.name
