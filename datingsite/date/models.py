from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    hobbies = models.CharField(max_length=200)
    music = models.CharField(max_length=100)
    short_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name
