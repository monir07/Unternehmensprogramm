# Generated by Django 2.0.13 on 2020-06-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0012_auto_20200626_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstore',
            name='ref_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
