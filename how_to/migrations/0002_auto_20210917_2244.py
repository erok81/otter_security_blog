# Generated by Django 3.2.7 on 2021-09-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('how_to', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='htmodel',
            options={'verbose_name': 'How to Post'},
        ),
        migrations.AddField(
            model_name='htmodel',
            name='summary',
            field=models.TextField(default='summary goes here'),
            preserve_default=False,
        ),
    ]