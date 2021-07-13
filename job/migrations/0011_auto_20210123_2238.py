# Generated by Django 3.1.5 on 2021-01-23 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0010_apply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apply',
            options={'verbose_name_plural': 'Apply'},
        ),
        migrations.AddField(
            model_name='job',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='auth.user'),
            preserve_default=False,
        ),
    ]