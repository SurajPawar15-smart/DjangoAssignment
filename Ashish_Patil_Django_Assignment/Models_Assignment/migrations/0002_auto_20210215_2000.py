# Generated by Django 3.1.5 on 2021-02-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models_Assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_accounts',
            name='Int_rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='loan_accounts',
            name='Loan_amount',
            field=models.FloatField(),
        ),
    ]