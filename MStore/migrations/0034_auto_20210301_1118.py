# Generated by Django 3.1.5 on 2021-03-01 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0033_auto_20210228_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120),
        ),
    ]