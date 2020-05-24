# Generated by Django 3.0.6 on 2020-05-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='update',
        ),
        migrations.AddField(
            model_name='link',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Red social'),
        ),
    ]
