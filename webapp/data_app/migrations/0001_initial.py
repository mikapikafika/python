# Generated by Django 5.0.1 on 2024-01-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature1', models.FloatField()),
                ('feature2', models.FloatField()),
                ('category', models.IntegerField()),
            ],
        ),
    ]
