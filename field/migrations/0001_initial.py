# Generated by Django 2.1.1 on 2018-11-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('REMOVE', models.BooleanField(default=False, null=True)),
                ('TITLE', models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
    ]
