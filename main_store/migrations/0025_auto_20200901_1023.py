# Generated by Django 2.0.13 on 2020-09-01 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0024_productissue_issuer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualitySignDgm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.ImageField(blank=True, null=True, upload_to='images/store/quality_sign/')),
            ],
        ),
        migrations.CreateModel(
            name='QualitySignShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.ImageField(blank=True, null=True, upload_to='images/store/quality_sign/')),
            ],
        ),
        migrations.CreateModel(
            name='QualitySignStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.ImageField(blank=True, null=True, upload_to='images/store/quality_sign/')),
            ],
        ),
        migrations.CreateModel(
            name='SignOicStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.ImageField(blank=True, null=True, upload_to='images/store/quality_sign/')),
            ],
        ),
        migrations.RemoveField(
            model_name='materialquality',
            name='dgm_sign',
        ),
        migrations.AlterField(
            model_name='materialquality',
            name='gm_sign',
            field=models.ManyToManyField(blank=True, to='main_store.QualitySign'),
        ),
        migrations.RemoveField(
            model_name='materialquality',
            name='oic_store_sign',
        ),
        migrations.RemoveField(
            model_name='materialquality',
            name='responsible_oic',
        ),
        migrations.RemoveField(
            model_name='materialquality',
            name='sign_oic_store',
        ),
        migrations.AddField(
            model_name='materialquality',
            name='dgm_sign',
            field=models.ManyToManyField(blank=True, to='main_store.QualitySignDgm'),
        ),
        migrations.AddField(
            model_name='materialquality',
            name='oic_store_sign',
            field=models.ManyToManyField(blank=True, to='main_store.QualitySignStore'),
        ),
        migrations.AddField(
            model_name='materialquality',
            name='responsible_oic',
            field=models.ManyToManyField(blank=True, to='main_store.QualitySignShop'),
        ),
        migrations.AddField(
            model_name='materialquality',
            name='sign_oic_store',
            field=models.ManyToManyField(blank=True, to='main_store.SignOicStore'),
        ),
    ]
