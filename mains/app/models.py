from django.db import models

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    rasm = models.ImageField(upload_to='img')

    def _str_(self):
        return self.username
    