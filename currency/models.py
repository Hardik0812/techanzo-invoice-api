from django.db import models

# Create your models here.
class Currency(models.Model):
    symbol = models.CharField(max_length=1)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name