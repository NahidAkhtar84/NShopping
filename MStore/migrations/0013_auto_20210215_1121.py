# Generated by Django 3.1.5 on 2021-02-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0012_auto_20210215_0048'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='variation',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120),
        ),
    ]
