# Generated by Django 3.1.5 on 2021-01-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20210123_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
