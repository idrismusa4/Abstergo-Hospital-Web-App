# Generated by Django 4.2.1 on 2023-05-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms_app', '0003_patient_user_alter_doctor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
