# Generated by Django 4.0.6 on 2022-08-01 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0003_alter_table_stickers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='todos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stickers.todo'),
        ),
    ]
