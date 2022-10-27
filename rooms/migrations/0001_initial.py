# Generated by Django 4.1.2 on 2022-10-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('country', models.CharField(default='South Korea', max_length=50)),
                ('city', models.CharField(default='Seoul', max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('rooms', models.PositiveIntegerField()),
                ('toilets', models.PositiveIntegerField()),
                ('kind', models.CharField(choices=[('entire place', 'Entire Place'), ('private room', 'Private Room'), ('shared room', 'Shared Room')], default='entire place', max_length=25)),
                ('amenities', models.ManyToManyField(to='rooms.amenity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
