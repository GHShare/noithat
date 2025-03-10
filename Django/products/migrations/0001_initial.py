# Generated by Django 5.1.6 on 2025-03-10 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryid', models.AutoField(db_column='categoryID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.AutoField(db_column='productID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('sold', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('categoryid', models.ForeignKey(blank=True, db_column='categoryID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
