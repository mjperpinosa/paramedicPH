# Generated by Django 2.1.4 on 2019-01-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20190108_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='username',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
