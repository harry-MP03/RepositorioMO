# Generated by Django 4.2 on 2024-10-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careunit',
            fields=[
                ('idCareunit', models.AutoField(primary_key=True, serialize=False)),
                ('nameCareUnit', models.CharField(max_length=30, verbose_name='Nombre de unidad de cuidado')),
            ],
            options={
                'verbose_name_plural': 'Unidades de cuidado',
            },
        ),
    ]
