# Generated by Django 5.1.5 on 2025-02-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_register_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='licence_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
