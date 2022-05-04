# Generated by Django 4.0.1 on 2022-01-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firsttitle', models.CharField(max_length=255)),
                ('firstpercent', models.IntegerField()),
                ('secondtitle', models.CharField(max_length=255)),
                ('secondpercent', models.IntegerField()),
                ('thirdtitle', models.CharField(max_length=255)),
                ('thirdpercent', models.IntegerField()),
                ('fourthtitle', models.CharField(max_length=255)),
                ('fourthpercent', models.IntegerField()),
                ('fivetitle', models.CharField(max_length=255)),
                ('fivepercent', models.IntegerField()),
                ('sixtitle', models.CharField(max_length=255)),
                ('sixpercent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SecondPageCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstnumber', models.IntegerField()),
                ('secondnumber', models.IntegerField()),
                ('thirdnumber', models.IntegerField()),
                ('fourthnumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WhoI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mycountry', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
    ]
