# Generated by Django 4.2 on 2023-04-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_post_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
