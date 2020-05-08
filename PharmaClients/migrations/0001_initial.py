# Generated by Django 3.0.5 on 2020-05-07 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('Added_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]