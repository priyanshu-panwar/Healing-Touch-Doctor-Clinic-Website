# Generated by Django 2.2.6 on 2020-05-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_appointment_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Gender'),
        ),
    ]
