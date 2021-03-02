from django.shortcuts import render, redirect
from django.http import  HttpResponse
from MStore.models.productModel import ProductModel
from MStore.models.categoryModel import Category
from MStore.models.tags import tags
from marketing.models import MarketingMessage
from MStore.models.customerModel import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from marketing.models import SliderHome, ScreensHome
from datetime import datetime, timedelta


# Create your views here.
class Index(View):
    def get(self, request):
        products = None
        categories = Category.get_all_catrgories()
        categoryId = request.GET.get('category')

        sliders = SliderHome.objects.all_featured()
        screens = ScreensHome.objects.all_featured()[:2]

        now = datetime.now()
        onemonthbefordate = now - timedelta(30)
        recent_products = ProductModel.objects.filter(uploaded__gte = onemonthbefordate)
        new_products = ProductModel.objects.filter(tags=1).all()
        summer_products = ProductModel.objects.filter(tags=2).all()
        print(new_products)

        if categoryId:
            products = ProductModel.get_all_product_byCategoryId(categoryId)
        else:
            products = ProductModel.get_all_product()
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['sliders'] = sliders
        data['screens'] = screens
        data['recentproducts'] = recent_products
        data['new_products'] = new_products
        data['summer_products'] = summer_products
        return render(request, 'index.html', data)

    def post(self, request):
        return redirect('homepage')








