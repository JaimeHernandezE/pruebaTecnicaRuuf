# Generated by Django 5.1.4 on 2024-12-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lado_a', models.FloatField()),
                ('lado_b', models.FloatField()),
                ('lado_x', models.FloatField()),
                ('lado_y', models.FloatField()),
                ('resultado', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
