# Generated by Django 4.2.1 on 2023-06-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0021_rename_number_qc_mus_number_qc_rat_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pc_ind',
            old_name='file',
            new_name='excel_file',
        ),
        migrations.RenameField(
            model_name='pc_ins',
            old_name='file',
            new_name='excel_file',
        ),
        migrations.RenameField(
            model_name='pc_ous',
            old_name='file',
            new_name='excel_file',
        ),
        migrations.RenameField(
            model_name='qc',
            old_name='file',
            new_name='excel_file',
        ),
        migrations.RenameField(
            model_name='sc',
            old_name='file',
            new_name='excel_file',
        ),
        migrations.AddField(
            model_name='pc_ind',
            name='pdf_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pc_ins',
            name='pdf_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pc_ous',
            name='pdf_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='qc',
            name='pdf_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sc',
            name='pdf_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
