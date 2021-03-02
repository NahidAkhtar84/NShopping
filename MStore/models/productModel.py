from django.db import models
from .categoryModel import Category
from django.urls import reverse
from django.utils import timezone
from .tags import tags

class Brand(models.Model):
    product = models.OneToOneField('ProductModel', on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='Uploads/brands/')

    def __str__(self):
        return self.brand

    @staticmethod
    def brand_count(brand):
        return Brand.objects.filter(brand = brand).count()

    @staticmethod
    def brand_image(brand):
        return Brand.objects.all().distinct('image')


class ProductModel(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1,)
    tags = models.ManyToManyField(tags, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    sales_price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00, null=True, blank=True)
    description = models.TextField(max_length=1200, default='', null=True, blank=True)
    slug = models.SlugField(unique=True, default="xyz")
    rating = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    sellingNumber = models.IntegerField(default=0)
    uploaded = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("singlepropa", kwargs={"slug": self.slug})

    class Meta:
        unique_together = ('name', 'slug')

    @staticmethod
    def get_all_product():
        return ProductModel.objects.all()

    @staticmethod
    def get_all_product_byCategoryId(category_id):
        if category_id:
            return ProductModel.objects.filter(category= category_id)
        else:
            return ProductModel.objects.all()

    @staticmethod
    def sort_all_product_byDate():
        try:
            return ProductModel.objects.order_by('uploaded')
        except:
            return ProductModel.objects.all()

    @staticmethod
    def get_product_by_cartids(ids):
        return ProductModel.objects.filter(id__in=ids)
