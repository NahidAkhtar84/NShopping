# Generated by Django 3.1.5 on 2021-02-16 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0015_auto_20210216_1649'),
        ('orders', '0002_auto_20210216_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MStore.customer'),
        ),
    ]
