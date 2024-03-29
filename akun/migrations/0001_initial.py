# Generated by Django 3.0.3 on 2020-03-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('jenis_kelamin', models.BooleanField()),
                ('kota_domisili', models.CharField(max_length=30)),
                ('alamat', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('tempat_lahir', models.CharField(max_length=30)),
                ('foto_path', models.CharField(max_length=200)),
                ('no_telepon', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('aktif', models.BooleanField()),
                ('registrasi', models.DateTimeField(auto_now_add=True)),
                ('aktivasi', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('admin', 'Admin'), ('staf', 'Staf'), ('member', 'Member')], default='member', max_length=6)),
            ],
        ),
    ]
