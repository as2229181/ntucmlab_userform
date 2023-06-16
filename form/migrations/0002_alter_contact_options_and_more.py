# Generated by Django 4.2.1 on 2023-06-08 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': '聯絡人', 'verbose_name_plural': '聯絡人'},
        ),
        migrations.AlterModelOptions(
            name='principal_investigator',
            options={'verbose_name': '實驗室負責人', 'verbose_name_plural': '實驗室負責人'},
        ),
        migrations.RenameField(
            model_name='principal_investigator',
            old_name='name',
            new_name='pi',
        ),
    ]
