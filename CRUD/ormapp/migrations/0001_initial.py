# Generated by Django 4.2.11 on 2024-04-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=20)),
                ('salary', models.FloatField()),
                ('aadhaar', models.BigIntegerField(null=True)),
            ],
        ),
    ]
