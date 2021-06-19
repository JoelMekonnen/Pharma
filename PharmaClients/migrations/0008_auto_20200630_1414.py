# Generated by Django 3.0.5 on 2020-06-30 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PharmaClients', '0007_drugorder_totalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(choices=[('Ethiopia', 'Ethiopia'), ('Kenya', 'Kenya'), ('Djbouti', 'Djbouti'), ('Somalia', 'Somalia'), ('Sudan', 'Sudan'), ('South Sudan', 'South Sudan'), ('Eritrea', 'Eritrea')], max_length=30)),
                ('City', models.CharField(max_length=100)),
                ('Street_Name', models.CharField(max_length=200)),
                ('House_No', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='druglist',
            name='price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='drugorder',
            name='Quantity',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='drugorder',
            name='Deliveries',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Delivery', to='PharmaClients.Delivery'),
        ),
    ]
