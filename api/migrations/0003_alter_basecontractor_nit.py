# Generated by Django 5.0.6 on 2024-06-18 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_basecontractor_basetransaction_remove_city_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basecontractor',
            name='nit',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
