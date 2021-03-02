from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from companyinfo.models import policies

class AboutUs(View):

    def get(self, request, tabinfo):
        policy = policies.objects.first()
        print('tabinfo', tabinfo)
        context = {
            'policy': policy,
            'tabinfo': tabinfo
        }
        return render(request, 'aboutus.html', context)
