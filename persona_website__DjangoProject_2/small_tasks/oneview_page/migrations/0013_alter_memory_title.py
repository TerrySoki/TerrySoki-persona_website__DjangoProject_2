# Generated by Django 4.1.1 on 2022-09-21 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneview_page', '0012_memory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='title',
            field=models.CharField(default='memory_title', max_length=100, primary_key=True, serialize=False),
        ),
    ]
