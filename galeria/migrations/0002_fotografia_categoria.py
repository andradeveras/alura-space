# Generated by Django 5.1.3 on 2024-11-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estela'), ('GALÁXIA', 'Galaxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]