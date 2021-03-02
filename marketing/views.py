from django.shortcuts import render
import json
from django.shortcuts import render, HttpResponse, Http404
from django.utils import timezone
import datetime
from django.conf import settings
from .forms import EmailForm
from django.http import HttpResponseBadRequest
from .models import emailMarketing

def dismiss_marketing(request):
    if request.is_ajax():
        data = {"success": True}
        print(data)
        json_data = json.dumps(data)
        request.session['dismiss_marketing'] = str(timezone.now() + datetime.timedelta(hours =settings.MARKETING_HOURS_OFFSET, seconds=settings.MARKETING_SECONDS_OFFSET))
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        raise Http404

def email_signup(request):
    if request.method == "POST":
        print(request.POST)
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_signup = emailMarketing.objects.create(email = email)
            request.session['email_added_marketing'] = True
            return HttpResponse('success %s' %(email))
        if form.errors:
            print(form.errors)
            json_data = json.dumps(form.errors)
            return HttpResponseBadRequest(json_data, content_type='application/json')
        else:
            return Http404
