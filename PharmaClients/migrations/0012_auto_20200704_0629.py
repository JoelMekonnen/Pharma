# Generated by Django 3.0.5 on 2020-07-04 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PharmaClients', '0011_auto_20200704_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugorder',
            name='Deliveries',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Deli', to='PharmaClients.Delivery'),
        ),
    ]