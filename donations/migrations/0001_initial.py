# Generated by Django 4.1 on 2022-10-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donation_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('mobile_no', models.CharField(max_length=12)),
                ('address', models.TextField()),
            ],
        ),
    ]
