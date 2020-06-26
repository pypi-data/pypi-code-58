# Generated by Django 2.2.4 on 2019-08-25 10:14

from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('clndr', '0056_auto_20190825_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar_shifts_days',
            name='saturday',
            field=isc_common.fields.related.ForeignKeyCascade(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_rel', to='clndr.Shift_day'),
        ),
        migrations.AlterField(
            model_name='calendar_shifts_days',
            name='friday',
            field=isc_common.fields.related.ForeignKeyCascade(on_delete=django.db.models.deletion.CASCADE, related_name='friday_rel', to='clndr.Shift_day'),
        ),
    ]
