from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(null=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.created_by = kwargs.get('user')
    #     self.save()
