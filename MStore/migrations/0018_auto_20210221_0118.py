# Generated by Django 3.1.5 on 2021-02-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0017_auto_20210218_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('package', 'package'), ('size', 'size'), ('color', 'color')], default='size', max_length=120),
        ),
    ]
