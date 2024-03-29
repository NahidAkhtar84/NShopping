# Generated by Django 3.1.5 on 2021-02-25 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0029_auto_20210226_0150'),
        ('orders', '0004_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDefaultAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_address_billing_default', to='orders.useraddress')),
                ('shipping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_address_shipping_default', to='orders.useraddress')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MStore.customer')),
            ],
        ),
    ]
