# Generated by Django 4.2.1 on 2023-05-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_alter_sc_scid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc_ind',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pc_ins',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pc_ous',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='qc',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sc',
            name='date',
            field=models.DateField(),
        ),
    ]