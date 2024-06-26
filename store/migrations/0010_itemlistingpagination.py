# Generated by Django 3.1.14 on 2022-11-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210525_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemListingPagination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_page', models.IntegerField(default=5, verbose_name='商品一覧')),
                ('category_page', models.IntegerField(default=5, verbose_name='カテゴリーページ')),
            ],
            options={
                'verbose_name': '商品一覧ページネーション',
                'verbose_name_plural': '商品一覧ページネーション',
            },
        ),
    ]
