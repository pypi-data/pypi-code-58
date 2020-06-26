# Generated by Django 2.1 on 2019-07-19 15:09

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0102_auto_20190719_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('default_flag', models.BooleanField(default=False)),
                ('inactive_flag', models.BooleanField(default=False)),
                ('spawn_followup_flag', models.BooleanField(default=False)),
                ('closed_flag', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
                ('default_flag', models.BooleanField(default=False)),
                ('inactive_flag', models.BooleanField(default=False)),
                ('email_flag', models.BooleanField(default=False)),
                ('memo_flag', models.BooleanField(default=False)),
                ('history_flag', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
