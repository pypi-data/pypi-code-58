# Generated by Django 2.2.2 on 2019-06-10 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one_c', '0007_remove_documents_param_1c_document'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='documents_param_1c',
            unique_together={('type', 'value')},
        ),
    ]
