# Generated by Django 3.1.5 on 2021-02-20 18:07

from django.db import migrations, models
import marketing.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(upload_to=marketing.models.slider_upload)),
                ('order', models.IntegerField(default=0)),
                ('button_text', models.CharField(blank=True, max_length=5, null=True)),
                ('button_link', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
