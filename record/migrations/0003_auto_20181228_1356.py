# Generated by Django 2.1.4 on 2018-12-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20181225_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyrecord',
            name='month',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyrecord',
            name='total_amount',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]