# Generated by Django 5.0.3 on 2024-03-20 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='dataset',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.dataset'),
        ),
    ]
