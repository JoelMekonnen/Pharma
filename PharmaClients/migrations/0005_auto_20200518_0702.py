# Generated by Django 3.0.5 on 2020-05-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PharmaClients', '0004_auto_20200518_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Drug_name', models.CharField(max_length=255)),
                ('Drug_Expiry', models.DateTimeField()),
                ('Drug_Manufacturer', models.CharField(max_length=255)),
                ('Preview', models.ImageField(upload_to='')),
                ('Drug_type', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('DateAdded', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FoodList',
        ),
    ]