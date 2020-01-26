# Generated by Django 3.0.2 on 2020-01-25 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20200125_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='places',
            name='name',
            field=models.CharField(default='NA', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='places',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Plan'),
        ),
    ]