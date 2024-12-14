# Generated by Django 4.2.16 on 2024-11-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_race_weapons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapons',
            old_name='damage',
            new_name='damage_medium',
        ),
        migrations.AddField(
            model_name='weapons',
            name='damage_small',
            field=models.CharField(default='-', max_length=10),
            preserve_default=False,
        ),
    ]
