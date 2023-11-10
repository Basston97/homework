from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    description = models.TextField(default='')
    counter = models.PositiveIntegerField(default=0)


