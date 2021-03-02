# Generated by Django 3.1.5 on 2021-03-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MStore', '0039_auto_20210302_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('color', 'color'), ('package', 'package'), ('size', 'size')], default='size', max_length=120),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(to='MStore.tags'),
        ),
    ]
