# Generated by Django 3.0.3 on 2020-02-06 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0078_delete_messages_theme_with_out_user_view'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ('lastmodified',), 'verbose_name': 'Сообщения'},
        ),
        migrations.RemoveField(
            model_name='messages',
            name='date_create',
        ),
    ]
