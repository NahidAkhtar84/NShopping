# Generated by Django 3.1.5 on 2021-02-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0023_auto_20210222_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('package', 'package'), ('color', 'color'), ('size', 'size')], default='size', max_length=120),
        ),
    ]
