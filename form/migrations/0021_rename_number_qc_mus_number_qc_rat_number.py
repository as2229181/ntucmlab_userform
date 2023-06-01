# Generated by Django 4.2.1 on 2023-05-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0020_rename_bloodcell_sc_cbc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qc',
            old_name='number',
            new_name='mus_number',
        ),
        migrations.AddField(
            model_name='qc',
            name='rat_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
