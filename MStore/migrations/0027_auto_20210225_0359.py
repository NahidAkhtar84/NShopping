# Generated by Django 3.1.5 on 2021-02-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0026_auto_20210223_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(to='MStore.Variation'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('package', 'package'), ('color', 'color')], default='size', max_length=120),
        ),
    ]