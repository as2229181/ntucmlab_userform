# Generated by Django 4.2.1 on 2023-05-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0016_remove_pc_ind_lab_tel_remove_pc_ind_pi'),
    ]

    operations = [
        migrations.AddField(
            model_name='pc_ind',
            name='file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pc_ins',
            name='file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pc_ous',
            name='file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sc',
            name='file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]