# Generated by Django 2.1.2 on 2018-11-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_mantencion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='NumTajeta',
            field=models.CharField(default=123456, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='TipoBanco',
            field=models.CharField(default=12345, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Trabajo',
            field=models.CharField(default=12345, max_length=200),
            preserve_default=False,
        ),
    ]
