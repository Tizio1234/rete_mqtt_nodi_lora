# Generated by Django 4.2.2 on 2023-06-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt_lora', '0005_alter_message_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.TextField(default='empty', max_length=512),
        ),
    ]