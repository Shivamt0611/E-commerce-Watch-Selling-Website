# Generated by Django 3.1 on 2020-09-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]