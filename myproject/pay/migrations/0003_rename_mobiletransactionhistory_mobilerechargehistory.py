# Generated by Django 5.1.4 on 2024-12-26 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_basetransaction_remove_user_account_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MobileTransactionHistory',
            new_name='MobileRechargeHistory',
        ),
    ]
