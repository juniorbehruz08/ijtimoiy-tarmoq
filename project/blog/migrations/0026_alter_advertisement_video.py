# Generated by Django 5.0 on 2024-03-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_advertisement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='advertisement', verbose_name='Video'),
        ),
    ]
