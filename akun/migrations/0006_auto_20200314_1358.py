# Generated by Django 3.0.3 on 2020-03-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0005_auto_20200310_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akun',
            name='aktif',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='akun',
            name='alamat',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akun',
            name='jenis_kelamin',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='akun',
            name='kota_domisili',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='akun',
            name='no_telepon',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='akun',
            name='tanggal_lahir',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='akun',
            name='tempat_lahir',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
