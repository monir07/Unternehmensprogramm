# Generated by Django 2.0.13 on 2020-06-13 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manhour', '0002_auto_20200613_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_manhour',
            name='manhour_otherShop',
        ),
        migrations.AddField(
            model_name='new_manhour',
            name='manhour_otherShop',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='manhour_otherShopName',
        ),
    ]
