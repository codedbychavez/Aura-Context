# Generated by Django 2.2.7 on 2020-05-14 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200310_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='bot_slots',
            field=models.CharField(default=None, max_length=500),
        ),
    ]