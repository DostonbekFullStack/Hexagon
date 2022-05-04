# Generated by Django 4.0.1 on 2022-01-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_sociallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('paragraph', models.CharField(max_length=255)),
                ('cardimg', models.ImageField(upload_to='blogcards')),
                ('cardtitle', models.CharField(max_length=255)),
                ('cardpara', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstnumber', models.IntegerField()),
                ('firstpara', models.CharField(max_length=255)),
                ('secondnumber', models.IntegerField()),
                ('secondpara', models.CharField(max_length=255)),
                ('thirdnumber', models.IntegerField()),
                ('thirdpara', models.CharField(max_length=255)),
                ('fourthnumber', models.IntegerField()),
                ('fourthpara', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('paragraph', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('paragraph', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UnderSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('underlogopara', models.CharField(max_length=255)),
                ('firstcolumntitle', models.CharField(max_length=255)),
                ('firstfirpara', models.CharField(max_length=255)),
                ('firstsecpara', models.CharField(max_length=255)),
                ('firstthipara', models.CharField(max_length=255)),
                ('firstfoupara', models.CharField(max_length=255)),
                ('secondcolumntitle', models.CharField(max_length=255)),
                ('secondfirpara', models.CharField(max_length=255)),
                ('secondsecpara', models.CharField(max_length=255)),
                ('secondthipara', models.CharField(max_length=255)),
                ('secondfoupara', models.CharField(max_length=255)),
                ('contactcolumntitle', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('firstlogo', models.CharField(max_length=255)),
                ('secondlogo', models.CharField(max_length=255)),
                ('thirdlogo', models.CharField(max_length=255)),
                ('fourthlogo', models.CharField(max_length=255)),
                ('fifthlogo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='firstlogo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='secondlogo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='thirdlogo',
            field=models.CharField(max_length=255),
        ),
    ]
