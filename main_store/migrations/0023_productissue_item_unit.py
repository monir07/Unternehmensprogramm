# Generated by Django 2.0.13 on 2020-08-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0022_auto_20200823_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='productissue',
            name='item_unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
