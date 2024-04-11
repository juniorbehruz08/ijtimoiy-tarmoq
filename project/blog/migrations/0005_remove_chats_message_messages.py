# Generated by Django 5.0 on 2024-03-09 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_accountphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='message',
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500, verbose_name='Message Text')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.chats', verbose_name='messages')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]