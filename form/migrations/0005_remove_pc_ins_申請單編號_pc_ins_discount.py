# Generated by Django 4.2.1 on 2023-06-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_sc_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pc_ins',
            name='申請單編號',
        ),
        migrations.AddField(
            model_name='pc_ins',
            name='discount',
            field=models.CharField(blank=True, default='100%', max_length=6, null=True),
        ),
    ]
