# Generated by Django 5.0 on 2024-03-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_chats_message_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='chat',
        ),
        migrations.DeleteModel(
            name='Chats',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]
