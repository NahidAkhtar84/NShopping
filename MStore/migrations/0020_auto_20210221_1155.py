# Generated by Django 3.1.5 on 2021-02-21 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0019_auto_20210221_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='brand',
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='Uploads/brands/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MStore.productmodel')),
            ],
        ),
    ]
