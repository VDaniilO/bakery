# Generated by Django 4.1.7 on 2023-03-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductOrder',
            new_name='OrderProduct',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
