# Generated by Django 4.2.1 on 2023-05-18 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_alter_pc_ind_date_alter_pc_ins_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pc_ind',
            old_name='pcid',
            new_name='pc_ind_id',
        ),
        migrations.RenameField(
            model_name='pc_ins',
            old_name='pcid',
            new_name='pc_ins_id',
        ),
        migrations.RenameField(
            model_name='pc_ous',
            old_name='pcid',
            new_name='pc_out_id',
        ),
    ]
