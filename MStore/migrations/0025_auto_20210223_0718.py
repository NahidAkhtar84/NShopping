# Generated by Django 3.1.5 on 2021-02-23 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0024_auto_20210223_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('package', 'package'), ('color', 'color')], default='size', max_length=120),
        ),
    ]