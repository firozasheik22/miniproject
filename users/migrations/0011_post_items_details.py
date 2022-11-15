# Generated by Django 4.1 on 2022-11-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_donor_table_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_items_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20, null=True)),
                ('item_type', models.CharField(max_length=20, null=True)),
                ('item_desc', models.CharField(max_length=200, null=True)),
                ('donor_username', models.CharField(max_length=12, null=True)),
                ('donor_mobile_no', models.CharField(max_length=12, null=True)),
                ('donor_address', models.TextField()),
                ('volunteer_username', models.CharField(max_length=12, null=True)),
                ('volunteer_mobile_no', models.CharField(max_length=12, null=True)),
                ('volunteer_address', models.TextField()),
            ],
        ),
    ]
