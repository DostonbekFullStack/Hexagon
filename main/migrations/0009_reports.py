# Generated by Django 4.0.1 on 2022-01-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_reservation_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='reservation')),
                ('title', models.CharField(max_length=255)),
                ('paragraph', models.CharField(max_length=255)),
                ('firstpara', models.CharField(max_length=255)),
                ('secondpara', models.CharField(max_length=255)),
                ('thirdpara', models.CharField(max_length=255)),
            ],
        ),
    ]