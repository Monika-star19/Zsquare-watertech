# Generated by Django 5.0.6 on 2024-07-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_productinquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicebooking',
            name='service',
            field=models.CharField(choices=[('ro', 'Domestic RO Service'), ('industrial', 'Industrial Ro Service'), ('commercial', 'Commercial Ro Service'), ('conditioner', 'Water Conditioner Service'), ('softner', 'Water Softener Service'), ('presure', 'Pressure Pump Service'), ('heat', 'Heat Pump Service'), ('pool', 'Swimming Pool Filtration Service'), ('ionizer', 'Water Ionizer Service'), ('rain', 'Rain Water Harvesting Service'), ('etp/stp', 'ETP/STP Service'), ('amc', 'AMC Service')], max_length=20),
        ),
    ]
