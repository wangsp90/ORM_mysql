# Generated by Django 2.1.1 on 2018-11-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fkey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='LEVEL',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]