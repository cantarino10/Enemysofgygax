# Generated by Django 4.2.16 on 2024-11-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0007_carrying'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrying',
            name='str',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
