# Generated by Django 3.2.5 on 2021-07-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_law_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='law',
            name='Category',
        ),
        migrations.AddField(
            model_name='law',
            name='Category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
