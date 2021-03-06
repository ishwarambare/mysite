# Generated by Django 3.0.8 on 2020-12-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201201_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, null=True),
        ),
    ]
