# Generated by Django 2.2.4 on 2021-07-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridapp', '0003_response_lastseenalive'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='DomainInfo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
