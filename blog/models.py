from django.db import models
from django.urls import reverse

class Persona(models.Model):
    nombre = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])
