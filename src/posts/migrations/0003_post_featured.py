# Generated by Django 3.0.4 on 2020-04-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]