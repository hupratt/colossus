# Generated by Django 2.0.7 on 2018-07-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20180729_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriberimport',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Queued'), (3, 'Importing'), (4, 'Completed'), (5, 'Errored'), (6, 'Canceled')], default=1, verbose_name='status'),
        ),
    ]
