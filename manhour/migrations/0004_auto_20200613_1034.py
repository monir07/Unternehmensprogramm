# Generated by Django 2.0.13 on 2020-06-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manhour', '0003_auto_20200613_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_manhour',
            old_name='manhour_otherShop',
            new_name='manhour_grinder_Other',
        ),
        migrations.AddField(
            model_name='new_manhour',
            name='manhour_fitter_Other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='new_manhour',
            name='manhour_gasCutter_Other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='new_manhour',
            name='manhour_welder_Other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
