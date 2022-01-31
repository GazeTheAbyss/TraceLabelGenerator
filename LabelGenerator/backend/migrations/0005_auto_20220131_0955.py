# Generated by Django 3.2.8 on 2022-01-31 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20220130_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='traceinformation',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='spaninformation',
            name='duration',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='spaninformation',
            name='parent_span_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='spaninformation',
            name='span_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='spaninformation',
            name='span_start_timestamp',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='traceinformation',
            name='trace_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='traceinformation',
            name='trace_start_timestamp',
            field=models.BigIntegerField(),
        ),
    ]
