from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='ND', null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)
    photo = models.ImageField(upload_to='contacts_photos/', null=True)

    def __str__(self):
        return self.name
