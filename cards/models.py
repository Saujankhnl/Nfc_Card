from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    photo = models.ImageField(upload_to='images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
