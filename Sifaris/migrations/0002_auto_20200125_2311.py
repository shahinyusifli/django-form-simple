# Generated by Django 3.0 on 2020-01-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sifaris', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olcu',
            name='title',
            field=models.CharField(choices=[('BALACA', 'Balaca'), ('ORTA', 'Orta'), ('BOYUK', 'Boyuk')], default='BOYUK', max_length=10),
        ),
    ]
