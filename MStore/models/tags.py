from django.db import models


class tags(models.Model):
    tag = models.CharField(max_length=70)

    def __str__(self):
        return self.tag
