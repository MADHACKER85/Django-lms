# Generated by Django 4.2.5 on 2024-04-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_file_remove_courseresource_file_courseresource_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseresource',
            name='files',
        ),
        migrations.AddField(
            model_name='courseresource',
            name='file',
            field=models.FileField(default='path/to/default/file.pdf', upload_to='course_resources/'),
        ),
    ]