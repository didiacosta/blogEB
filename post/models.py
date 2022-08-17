from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    #date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
