# Generated by Django 4.2.16 on 2024-11-02 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_races_traits'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Armor',
        ),
        migrations.DeleteModel(
            name='Classes',
        ),
        migrations.DeleteModel(
            name='Races',
        ),
        migrations.DeleteModel(
            name='Shield',
        ),
        migrations.DeleteModel(
            name='Weapons',
        ),
    ]
