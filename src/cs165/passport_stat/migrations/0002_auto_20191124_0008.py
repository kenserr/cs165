# Generated by Django 2.0.7 on 2019-11-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passport_stat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport_stat',
            name='extra_documents',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]