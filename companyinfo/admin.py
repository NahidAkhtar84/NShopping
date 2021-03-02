from django.contrib import admin
from .models import sociallinks, companyContactInformation, copyright, policies
# Register your models here.

class sociallinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'icon']

class companyContactInformationAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email']

admin.site.register(sociallinks, sociallinksAdmin)
admin.site.register(companyContactInformation, companyContactInformationAdmin)
admin.site.register(copyright)
admin.site.register(policies)