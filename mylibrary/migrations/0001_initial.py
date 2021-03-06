# Generated by Django 3.1.5 on 2021-02-01 20:34

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('images', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
