# Generated by Django 3.1.5 on 2021-03-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0035_auto_20210301_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('package', 'package'), ('size', 'size'), ('color', 'color')], default='size', max_length=120),
        ),
    ]
