# Generated by Django 3.2.7 on 2021-10-08 21:45

import adminlte.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to=adminlte.models.filepath),
        ),
    ]
