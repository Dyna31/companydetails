# Generated by Django 4.0.1 on 2022-02-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0003_rename_img_companydb_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydb',
            name='edit',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
