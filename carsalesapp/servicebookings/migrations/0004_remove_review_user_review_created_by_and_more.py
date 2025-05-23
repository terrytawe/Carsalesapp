# Generated by Django 5.2 on 2025-04-22 07:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_vehiclemodel_brand_alter_vehiclemodel_category'),
        ('servicebookings', '0003_customervehicle_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='moderated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews_moderated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='servicerecord',
            name='service_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testdriverecord',
            name='last_modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests_managed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testdriverecord',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='testdriverecord',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests_driven', to='inventory.vehiclemodel'),
        ),
    ]
