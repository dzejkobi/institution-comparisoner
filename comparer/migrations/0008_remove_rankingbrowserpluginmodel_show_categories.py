# Generated by Django 3.1.12 on 2021-07-08 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparer', '0007_auto_20210708_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rankingbrowserpluginmodel',
            name='show_categories',
        ),
    ]