# Generated by Django 4.0.3 on 2022-03-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0006_alter_lot_txid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='hash',
            field=models.CharField(blank=True, default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='lot',
            name='txId',
            field=models.CharField(blank=True, default=None, max_length=66),
        ),
    ]