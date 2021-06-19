# Generated by Django 3.0.5 on 2020-06-30 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PharmaClients', '0009_auto_20200630_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugorder',
            name='Deliveries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Delivery', to='PharmaClients.Delivery'),
        ),
    ]
