# Generated by Django 3.1 on 2020-09-10 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200910_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
    ]
