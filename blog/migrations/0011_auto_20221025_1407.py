# Generated by Django 3.1.8 on 2022-10-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210525_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpagination',
            name='whatsnew_home',
            field=models.IntegerField(default=3, verbose_name="What's New"),
        ),
    ]
