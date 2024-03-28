# Generated by Django 4.2.11 on 2024-03-28 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=5)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='apartments.apartment')),
            ],
        ),
    ]
