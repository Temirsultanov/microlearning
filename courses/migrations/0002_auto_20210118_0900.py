# Generated by Django 3.1.5 on 2021-01-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='queue',
            field=models.IntegerField(help_text='Введите место в очереди', verbose_name='Место в очереди'),
        ),
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.TextField(help_text='Введите контент карточки', max_length=1000, verbose_name='Контент карточки'),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(help_text='Введите заголовок карточки', max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.TextField(help_text='Введите описание курса', max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text='Введите название курса', max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='usersstats',
            name='time',
            field=models.DateField(null=True),
        ),
    ]
