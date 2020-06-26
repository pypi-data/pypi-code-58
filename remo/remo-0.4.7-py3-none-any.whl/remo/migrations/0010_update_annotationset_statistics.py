# Generated by Django 2.2.11 on 2020-06-22 15:13

from django.db import migrations

from remo_app.remo.use_cases.jobs import update_all_annotation_sets_statistics


def update_annotationset_statistics(apps, schema_editor):
    update_all_annotation_sets_statistics()


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0009_auto_20200622_1513'),
    ]

    operations = [
        migrations.RunPython(update_annotationset_statistics)
    ]
