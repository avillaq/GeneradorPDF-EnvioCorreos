# Generated by Django 5.0.6 on 2024-06-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnologia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('movies', models.ManyToManyField(to='tecnologia.movie')),
            ],
        ),
    ]
