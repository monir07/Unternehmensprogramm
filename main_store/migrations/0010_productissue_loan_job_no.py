# Generated by Django 2.0.13 on 2020-06-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0009_auto_20200623_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='productissue',
            name='loan_job_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
