# Generated by Django 5.2 on 2025-04-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='vehicle_features', to='inventory.feature'),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
