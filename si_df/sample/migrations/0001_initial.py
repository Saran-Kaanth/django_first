# Generated by Django 4.0.6 on 2022-08-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Production052022Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.IntegerField()),
                ('mill_date', models.DateTimeField()),
                ('mill_shift', models.IntegerField()),
                ('total_products', models.BigIntegerField()),
                ('total_run_time', models.DecimalField(blank=True, decimal_places=0, max_digits=32, null=True)),
                ('total_losses', models.DecimalField(blank=True, decimal_places=0, max_digits=32, null=True)),
                ('total_loss_1', models.DecimalField(blank=True, decimal_places=0, max_digits=32, null=True)),
                ('total_loss_2', models.DecimalField(blank=True, decimal_places=0, max_digits=32, null=True)),
                ('total_target', models.FloatField(blank=True, null=True)),
                ('total_actual', models.FloatField(blank=True, null=True)),
                ('total_goodqty', models.FloatField(blank=True, null=True)),
                ('total_errorqty', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'production_052022_shift',
                'managed': False,
            },
        ),
    ]
