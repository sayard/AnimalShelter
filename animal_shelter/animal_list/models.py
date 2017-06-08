from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=80)
    color = models.CharField(max_length=30)
    species = models.CharField(max_length=40)
    description = models.TextField(default='')
    description.null = False
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name
