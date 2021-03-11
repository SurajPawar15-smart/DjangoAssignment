# Generated by Django 3.1.5 on 2021-02-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accno', models.IntegerField()),
                ('Cust_name', models.CharField(max_length=20)),
                ('Loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Installments', models.IntegerField()),
                ('Int_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Start_date', models.DateField()),
                ('Interest', models.FloatField()),
            ],
        ),
    ]
