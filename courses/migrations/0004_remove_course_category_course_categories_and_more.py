# Generated by Django 5.0.6 on 2024-06-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='courses.categories'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
