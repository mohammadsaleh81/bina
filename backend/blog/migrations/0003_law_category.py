# Generated by Django 3.2.5 on 2021-07-25 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210725_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='law',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
            preserve_default=False,
        ),
    ]
