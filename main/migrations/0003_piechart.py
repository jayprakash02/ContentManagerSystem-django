# Generated by Django 3.0.3 on 2020-06-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_chart_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piechart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('c', models.IntegerField()),
            ],
        ),
    ]