# Generated by Django 3.1 on 2020-09-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile_number',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]