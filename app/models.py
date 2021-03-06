from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField()
    author = models.CharField(max_length=200, default="Anonymous")
    email = models.EmailField(blank=True)
    describe = models.TextField(default="Empty Book")
    
    def __str__(self):
        return self.name