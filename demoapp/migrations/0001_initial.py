# Generated by Django 3.0.8 on 2021-02-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='Enter Your First Name')),
                ('lname', models.CharField(max_length=50, verbose_name='Enter Your Last Name')),
                ('gender', models.CharField(max_length=10, verbose_name='Choose Your Gender')),
                ('emailid', models.EmailField(max_length=250, verbose_name='Enter Your Email Id')),
                ('phone', models.IntegerField(verbose_name='Enetr Your Mobile Number')),
            ],
        ),
    ]
