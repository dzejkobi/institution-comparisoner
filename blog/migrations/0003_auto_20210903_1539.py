# Generated by Django 3.1.12 on 2021-09-03 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('blog', '0002_auto_20210903_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogRecentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='blog_blogrecentpluginmodel', serialize=False, to='cms.cmsplugin')),
                ('post_count', models.PositiveSmallIntegerField(default=3, verbose_name='number of posts')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='blogindexpluginmodel',
            name='more_title',
            field=models.CharField(default='Read more blog posts', help_text='Title of the remaining posts section.', max_length=250, verbose_name='remaining posts title'),
        ),
    ]