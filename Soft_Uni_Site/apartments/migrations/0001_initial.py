# Generated by Django 4.2.11 on 2024-03-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bedrooms', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('image_url', models.URLField(verbose_name='Image URL:')),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
