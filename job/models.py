from django.db import models

 #Create your models here.
class job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.TextField(max_length = 200)

    def __str__(self):
        return self.summary[:2]

    def summ(self):
        return self.summary[:5]
