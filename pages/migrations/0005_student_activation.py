# Generated by Django 4.0.4 on 2022-05-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_student_activation'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='activation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
