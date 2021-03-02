from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, default="fa fa-tshirt")

    @staticmethod
    def get_all_catrgories():
        return Category.objects.all()

    def __str__(self):
        return self.name