from django.db import models

class User(models.Model):
    def __str__(self):
        return "{} {}: {}".format(self.first_name, self.last_name, self.email)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.DateTimeField('time created')


class Item(models.Model):
    def __str__(self):
        return "{}: {}".format(self.name, self.price)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField('time created')
