from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, default='0')
    email = models.EmailField()
    password = models.CharField(max_length=40)
    def __str__(self):
        return self.first_name


    def register(self):
        self.save()

    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    @staticmethod
    def loginCustomer(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False