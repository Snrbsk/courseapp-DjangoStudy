# Generated by Django 5.0.6 on 2024-06-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_ishome_alter_course_isactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
