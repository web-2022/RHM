# Generated by Django 5.1.7 on 2025-04-08 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_lesson_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='template',
            field=models.CharField(default='course/leccion1.html', help_text='Ejemplo: course/leccion1.html', max_length=100),
        ),
    ]
