# Generated by Django 3.1.1 on 2021-10-27 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kiddies_app', '0005_auto_20211027_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tblorder',
            old_name='order_id',
            new_name='order_no',
        ),
        migrations.RemoveField(
            model_name='tblorder',
            name='order_qty',
        ),
        migrations.RemoveField(
            model_name='tblorder',
            name='product_id',
        ),
    ]
