# Generated by Django 3.1 on 2020-09-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200910_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(blank=True, default='', max_length=6),
        ),
    ]