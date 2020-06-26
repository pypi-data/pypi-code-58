# Generated by Django 2.2.11 on 2020-04-16 09:40

from django.db import migrations, models
import remo_app.remo.models.dataset


class Migration(migrations.Migration):

    dependencies = [
        ('remo', '0003_remove_annotationset_strict_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='datasetimage',
            name='original_name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='download',
            name='file_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(max_length=1000, null=True, upload_to=remo_app.remo.models.dataset.get_image_file_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='original',
            field=models.FileField(max_length=1000, null=True, upload_to=remo_app.remo.models.dataset.get_original_file_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='preview',
            field=models.FileField(max_length=1000, null=True, upload_to=remo_app.remo.models.dataset.get_preview_file_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.FileField(max_length=1000, null=True, upload_to=remo_app.remo.models.dataset.get_thumbnail_file_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='view',
            field=models.FileField(max_length=1000, null=True, upload_to=remo_app.remo.models.dataset.get_view_file_path),
        ),
    ]
