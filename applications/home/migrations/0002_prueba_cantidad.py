# Generated by Django 4.2.2 on 2023-06-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
