from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings

# Create your models here.
class MarketingMessageQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)\
        .filter(start_date__lt = timezone.now())\
        .filter(end_date__gte = timezone.now())


class MarketingMessageManager(models.Manager):
    def get_queryset(self):
        return MarketingMessageQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def all_featured(self):
        return self.get_queryset().active().featured()

    def get_featured_item(self):
        try:
            return self.get_queryset().active().featured().order_by("start_date")[0]
        except:
            return None


class MarketingMessage(models.Model):
    message = models.TextField(max_length=600)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = MarketingMessageManager()

    def __str__(self):
        return self.message[:12]


# slider
def slider_upload(instance, filename):
    return "Uploads/sliders/%s" %(filename)

class SliderHome(models.Model):
    header = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to=slider_upload)
    order = models.IntegerField(default=0)
    button_text = models.CharField(max_length=30, null=True, blank=True)
    url_link = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    objects = MarketingMessageManager()

    def __str__(self):
        return self.header
    class Meta:
        ordering = ['order']

    def get_image_url(self):
        return "%s/%s" %(settings.MEDIA_URL, self.image)


class emailMarketing(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email


def screen_upload(instance, filename):
    return "Uploads/screens/%s" %(filename)

class ScreensHome(models.Model):
    header = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=screen_upload)
    order = models.IntegerField(default=0)
    url_link = models.CharField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    objects = MarketingMessageManager()

    def get_image_url(self):
        return "%s/%s" %(settings.MEDIA_URL, self.image)