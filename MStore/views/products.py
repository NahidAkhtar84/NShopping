from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from marketing.models import SliderHome
from django.shortcuts import render, redirect
from django.http import HttpResponse
from MStore.models.productModel import ProductModel, Brand
from MStore.models.categoryModel import Category
from django.core.paginator import Paginator, EmptyPage
from datetime import datetime


class Products(View):
    def get(self, request):
        products = None
        brands = Brand.objects.values('brand').distinct()
        categories = Category.get_all_catrgories()
        categoryId = request.GET.get('category')
        productstate = request.GET.get('productstate')
        prerange = request.GET.get('prerange')
        postrange = request.GET.get('postrange')
        data = {}

        if categoryId:
            products = ProductModel.get_all_product_byCategoryId(categoryId)
        elif productstate == "newest":
            products = ProductModel.sort_all_product_byDate()
        elif prerange and postrange:
            products = ProductModel.objects.filter(price__gte = prerange, price__lte = postrange)
        else:
            products = ProductModel.get_all_product()

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 9)

        try:
            products = paginator.page(page)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        data['products'] = products
        data['categories'] = categories
        data['brands'] = brands
        return render(request, 'products.html', data)

    def post(self, request):
        return redirect('products')
