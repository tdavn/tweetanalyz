# Generated by Django 3.2.7 on 2021-11-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet_store',
            name='tweet_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]