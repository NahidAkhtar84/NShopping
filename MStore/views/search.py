from django.shortcuts import render
from django.views import View
from MStore.models.productModel import ProductModel
#login class
class Search(View):
    def get(self, request):
        try:
            q = request.GET.get('q')
        except:
            q = None

        if q:
            products = ProductModel.objects.filter(name__icontains=q)
            context = {'query': q, 'products': products}
            template = 'results.html'
        else:
            template = 'index.html'
            context = {}

        return render(request, template, context)