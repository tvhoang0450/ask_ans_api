# Generated by Django 3.0.8 on 2021-03-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]