# Generated by Django 2.1.1 on 2018-11-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='NAME',
            field=models.CharField(max_length=255),
        ),
    ]
