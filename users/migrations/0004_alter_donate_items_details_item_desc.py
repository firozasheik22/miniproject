# Generated by Django 4.1 on 2022-10-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_donate_items_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate_items_details',
            name='item_desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]