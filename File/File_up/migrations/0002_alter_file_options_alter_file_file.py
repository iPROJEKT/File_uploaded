# Generated by Django 4.2.5 on 2023-09-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File_up', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=250, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]