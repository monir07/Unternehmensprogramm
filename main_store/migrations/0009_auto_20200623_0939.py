# Generated by Django 2.0.13 on 2020-06-23 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0008_auto_20200622_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstore',
            name='item_unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productstore',
            name='item_user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
