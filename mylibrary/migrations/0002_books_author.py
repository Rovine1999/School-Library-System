# Generated by Django 3.1.5 on 2021-02-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]