# Generated by Django 5.0.1 on 2024-01-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myflixapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[('single', 'Single'), ('seasonal', 'Seasonal')], max_length=10),
        ),
    ]
