# Generated by Django 4.2.1 on 2023-11-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_subset_basic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='set',
            old_name='codice',
            new_name='code',
        ),
    ]
