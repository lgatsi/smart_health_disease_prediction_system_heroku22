# Generated by Django 3.2.19 on 2023-06-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Zimbabwe', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_manage',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
