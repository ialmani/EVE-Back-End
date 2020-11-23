from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)

    def __str__(self):
        return self.title
