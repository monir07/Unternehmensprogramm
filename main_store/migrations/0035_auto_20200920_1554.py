# Generated by Django 2.0.13 on 2020-09-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0034_auto_20200919_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='indent',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='indentmaterials',
            name='indent_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
