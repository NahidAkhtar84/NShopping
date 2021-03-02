from django.contrib import admin
from .models import MarketingMessage, SliderHome, emailMarketing, ScreensHome
# Register your models here.

# class AdminCustomer(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'password']

class SliderDisplay(admin.ModelAdmin):
    list_display = ['header', 'image', 'order', 'description', 'button_text', 'url_link', 'active', 'featured', 'start_date', 'end_date']
    list_editable = ['order', 'start_date', 'end_date']

class MarketingMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = MarketingMessage

class emai_marketing(admin.ModelAdmin):
    list_display = ['email', 'timestamp']
    class Meta:
        model = emailMarketing

class ScreenAdmin(admin.ModelAdmin):
    list_display = ['header', 'image', 'order', 'url_link', 'active', 'featured', 'start_date', 'end_date']
    list_editable = ['order', 'start_date', 'end_date']
    class Meta:
        model = ScreensHome

admin.site.register(MarketingMessage, MarketingMessageAdmin)
admin.site.register(SliderHome, SliderDisplay)
admin.site.register(emailMarketing, emai_marketing)
admin.site.register(ScreensHome, ScreenAdmin)