# Generated by Django 4.2.16 on 2024-11-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_armor_weight_shield_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='book',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
