# Generated by Django 3.0.6 on 2020-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0002_pick_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='year',
            field=models.IntegerField(default=2020),
            preserve_default=False,
        ),
    ]