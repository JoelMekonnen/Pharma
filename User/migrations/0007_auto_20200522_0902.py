# Generated by Django 3.0.5 on 2020-05-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20200522_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
