from django.db import models

# Create your models here.

class sociallinks(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=600)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class companyContactInformation(models.Model):
    phone = models.CharField(max_length=20, default='0120000000000')
    email = models.EmailField(max_length=400)
    address = models.TextField(max_length=1000)

    def __str__(self):
        return self.address

class copyright(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=600, default='xyz')

    def __str__(self):
        return self.name

class policies(models.Model):
    aboutus = models.TextField(max_length=2000)
    privacy_policy = models.TextField(max_length=2000)
    terms_conditions = models.TextField(max_length=2000)
    payment_policy = models.TextField(max_length=2000)
    shipping_policy = models.TextField(max_length=2000)
    return_policy = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.id)
