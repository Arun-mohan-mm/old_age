# Generated by Django 5.0.3 on 2024-03-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldd', '0003_rename_category_category_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
