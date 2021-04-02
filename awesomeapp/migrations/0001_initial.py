# Generated by Django 3.1.7 on 2021-03-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
