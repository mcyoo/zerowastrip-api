# Generated by Django 3.1.7 on 2021-05-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cafe',
            old_name='meeting_time',
            new_name='special_holiday',
        ),
        migrations.AddField(
            model_name='cafe',
            name='check_time',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='image4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='image5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]