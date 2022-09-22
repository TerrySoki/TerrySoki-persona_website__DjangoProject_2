# Generated by Django 4.1.1 on 2022-09-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneview_page', '0005_mtv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Me',
            fields=[
                ('image_file', models.ImageField(upload_to='')),
                ('title', models.CharField(default='mtv_title', max_length=100, primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=200, null=True)),
                ('age', models.FloatField()),
                ('created_date_time', models.DateTimeField()),
                ('edited_finished_date_time', models.DateTimeField(null=True)),
                ('what_I_am_thinking', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mtv',
            name='title',
            field=models.CharField(default='mtv_title', max_length=100, primary_key=True, serialize=False),
        ),
    ]