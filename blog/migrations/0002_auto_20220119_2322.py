# Generated by Django 3.2.11 on 2022-01-19 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imag',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='Subtitle', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
