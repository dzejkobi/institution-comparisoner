# Generated by Django 3.1.12 on 2021-08-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparer', '0018_auto_20210826_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='policycriterion',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
