# Generated by Django 4.2.1 on 2023-08-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("form", "0015_alter_pc_ind_pc_ind_id_alter_pc_ous_pc_out_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pcid",
            options={"verbose_name": "切片表單編號", "verbose_name_plural": "切片表單編號"},
        ),
        migrations.AddField(
            model_name="ms",
            name="L",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="pc_ind",
            name="L",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="pc_ins",
            name="L",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="pc_ous",
            name="L",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
