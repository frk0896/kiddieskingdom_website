# Generated by Django 3.2.5 on 2021-10-25 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kiddies_app', '0003_tblorder_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tblorder_details',
            old_name='cust_id',
            new_name='user_id',
        ),
    ]
