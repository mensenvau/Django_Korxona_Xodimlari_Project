# Generated by Django 3.1.14 on 2023-01-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xodim', '0004_auto_20230102_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='position',
            field=models.CharField(default='DEFAULT VALUE', max_length=200),
        ),
    ]
