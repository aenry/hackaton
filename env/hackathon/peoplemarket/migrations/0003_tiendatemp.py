# Generated by Django 3.2.4 on 2021-06-26 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peoplemarket', '0002_auto_20210626_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiendaTemp',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=25)),
                ('logo', models.CharField(max_length=255)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peoplemarket.comuna')),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peoplemarket.rubro')),
            ],
        ),
    ]