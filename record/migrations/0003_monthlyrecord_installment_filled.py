# Generated by Django 2.1.4 on 2019-01-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20190107_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyrecord',
            name='installment_filled',
            field=models.BooleanField(default=False),
        ),
    ]