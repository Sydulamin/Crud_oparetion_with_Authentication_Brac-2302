from django.db import models

# Create your models here.

class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Profpic/', default='defult/defult.jpg', null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=25, null=True, blank=True)
    Birth_day = models.TextField()
    Gender = models.CharField(choices=GENDER, max_length=6)
    phone_number = models.TextField()
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)