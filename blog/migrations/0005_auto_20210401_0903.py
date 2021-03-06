# Generated by Django 3.1.7 on 2021-04-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210401_0508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag'),
        ),
    ]
