# Generated by Django 2.0.13 on 2020-07-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0019_auto_20200707_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialquality',
            name='gm_sign',
            field=models.ManyToManyField(blank=True, null=True, to='main_store.QualitySign'),
        ),
    ]
