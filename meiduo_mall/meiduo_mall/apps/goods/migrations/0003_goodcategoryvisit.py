# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-03 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190701_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodCategoryVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='访问日期')),
                ('count', models.IntegerField(default=0, verbose_name='访问量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_counts', to='goods.GoodsCategory', verbose_name='商品分类')),
            ],
            options={
                'db_table': 'tb_goods_category_visit',
            },
        ),
    ]
