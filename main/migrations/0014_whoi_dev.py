# Generated by Django 4.0.1 on 2022-01-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_myskills_secondpagecount_whoi'),
    ]

    operations = [
        migrations.AddField(
            model_name='whoi',
            name='dev',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
    ]
