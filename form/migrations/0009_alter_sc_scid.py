# Generated by Django 4.2.1 on 2023-05-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_alter_sc_scid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sc',
            name='scid',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
    ]