# Generated by Django 3.0.3 on 2020-03-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0005_auto_20200314_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='logo_src',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='konten',
            field=models.TextField(null=True),
        ),
    ]
