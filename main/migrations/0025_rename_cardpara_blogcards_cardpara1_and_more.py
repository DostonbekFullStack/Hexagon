# Generated by Django 4.0.1 on 2022-01-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_blogcards_cardlink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcards',
            old_name='cardpara',
            new_name='cardpara1',
        ),
        migrations.AddField(
            model_name='blogcards',
            name='cardpara2',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
    ]
