# Generated by Django 5.0 on 2024-03-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_like_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]