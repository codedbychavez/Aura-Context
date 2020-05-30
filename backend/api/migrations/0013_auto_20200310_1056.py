# Generated by Django 3.0.4 on 2020-03-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_intent_intent_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='svp',
            name='svp',
        ),
        migrations.AddField(
            model_name='svp',
            name='slots',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='svp',
            name='svp_data',
            field=models.CharField(default='', max_length=2056),
        ),
        migrations.AddField(
            model_name='svp',
            name='utterance',
            field=models.CharField(default='', max_length=2056),
        ),
    ]