# Generated by Django 4.2.4 on 2023-08-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRentCar', '0009_remove_rentalterms_price_rentalterms_premium_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='cars_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Van', 'Van'), ('Suv', 'Suv'), ('Kombi', 'Kombi'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Shooting brake', 'Shooting brake')], max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='drive',
            field=models.CharField(choices=[('Tylni', 'Tylni'), ('4x4', '4x4'), ('Przedni', 'Przedni')], max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(choices=[('Hybryda', 'Hybryda'), ('Elektryczny', 'Elektryczny'), ('Diesel', 'Diesel'), ('Benzyna', 'Benzyna')], max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_gears',
            field=models.CharField(choices=[('5', '5'), ('7', '7'), ('6', '6'), ('8', '8')], max_length=8),
        ),
    ]
