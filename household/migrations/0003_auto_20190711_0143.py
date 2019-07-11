# Generated by Django 2.2.3 on 2019-07-11 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0002_remove_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='asset_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='household.Asset'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_to_be_performed_by',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_of_allocation',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='task',
            name='worker_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='household.Worker'),
        ),
    ]
