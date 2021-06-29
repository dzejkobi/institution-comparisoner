# Generated by Django 3.1.12 on 2021-06-29 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('comparer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankingBoxPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='comparer_rankingboxpluginmodel', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='title')),
                ('items_count', models.PositiveSmallIntegerField(default=5, verbose_name='items count')),
                ('country_filter', models.CharField(blank=True, help_text='You can type more than one (separated with semicolon).', max_length=250, verbose_name='filter by countries')),
                ('html_classes', models.CharField(blank=True, max_length=250, verbose_name='HTML classes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]