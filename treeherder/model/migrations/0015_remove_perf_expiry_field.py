# Generated by Django 2.1.7 on 2019-03-13 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0014_add_job_log_status_skipped_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='expire_performance_data',
        ),
    ]