# Generated by Django 4.0.2 on 2022-03-10 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0003_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='pub_date',
        ),
    ]
