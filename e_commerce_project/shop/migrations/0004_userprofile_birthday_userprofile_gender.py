# Generated by Django 4.2.7 on 2023-11-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]