# Generated by Django 4.0.1 on 2022-01-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_youtubelink'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessSucces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('paragraph', models.CharField(max_length=400)),
            ],
        ),
    ]
