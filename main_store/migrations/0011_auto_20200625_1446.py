# Generated by Django 2.0.13 on 2020-06-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0010_productissue_loan_job_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstore',
            name='item_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/store/product/'),
        ),
        migrations.AddField(
            model_name='productstore',
            name='recorder',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
