# Generated by Django 3.1.7 on 2021-04-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=50)),
                ('open_time', models.TimeField(default='00:00:00')),
                ('close_time', models.TimeField(default='00:00:00')),
                ('holiday', models.CharField(choices=[('Monday', '월요일'), ('Tuesday', '화요일'), ('Wednesday', '수요일'), ('Thursday', '목요일'), ('Friday', '금요일'), ('Saturday', '토요일'), ('Sunday', '일요일')], default='Monday', max_length=16)),
                ('meeting_time', models.DateField()),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10)),
                ('content', models.TextField()),
                ('file1', models.ImageField(upload_to='')),
                ('file2', models.ImageField(upload_to='')),
                ('file3', models.ImageField(upload_to='')),
                ('file4', models.ImageField(upload_to='')),
            ],
        ),
    ]
