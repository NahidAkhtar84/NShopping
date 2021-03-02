from django.shortcuts import render, redirect, HttpResponseRedirect
from MStore.models.productModel import ProductModel, Brand
from django.contrib.auth.hashers import check_password
from django.views import View
from MStore.models.categoryModel import Category

#login class
class SinglePropa(View):

    def get(self, request, slug):
        categories = Category.get_all_catrgories()
        product = ProductModel.objects.get(slug = slug)
        products = ProductModel.get_all_product()
        brands = Brand.objects.values('brand').distinct()
        context = {'product': product,
                   'categories': categories,
                   'products': products,
                   'brands': brands,
                   }
        return render(request, 'singlepropa.html', context)
