# Generated by Django 5.0 on 2024-03-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='advertisement', verbose_name='Video')),
                ('image', models.ImageField(upload_to='advertisement', verbose_name='image')),
                ('price', models.IntegerField(default=0)),
                ('period', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
            },
        ),
    ]
