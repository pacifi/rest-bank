# Generated by Django 2.1.7 on 2019-02-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_auto_20190223_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]