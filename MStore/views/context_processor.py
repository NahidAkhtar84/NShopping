from companyinfo.models import sociallinks, companyContactInformation, copyright

def context_processor(request):
    social = sociallinks.objects.all()
    address =  companyContactInformation.objects.first()
    copyrght = copyright.objects.first()
    contextview = {
        'social': social,
        'address': address,
        'copyrght': copyrght,
    }

    return contextview