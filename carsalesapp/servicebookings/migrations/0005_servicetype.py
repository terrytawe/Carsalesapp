# Generated by Django 5.2 on 2025-04-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicebookings', '0004_remove_review_user_review_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
