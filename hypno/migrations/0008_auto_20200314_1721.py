# Generated by Django 3.0.3 on 2020-03-14 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hypno', '0007_auto_20200311_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='paket_terapi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio', to='hypno.PaketTerapi'),
        ),
    ]
