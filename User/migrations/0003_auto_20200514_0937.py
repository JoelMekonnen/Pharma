# Generated by Django 3.0.5 on 2020-05-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20200514_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_Image',
            field=models.ImageField(storage='<django.db.models.query_utils.DeferredAttribute object at 0x0000017DC4286B88>/', upload_to=''),
        ),
    ]