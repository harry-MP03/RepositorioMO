# Generated by Django 4.2 on 2024-10-26 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TiposBebida', '0001_initial'),
        ('Bebidas', '0003_beverages_typebeveragesfk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverages',
            name='typeBeveragesFK',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='TiposBebida.typebeverage', verbose_name='Tipo de bebida'),
        ),
    ]
