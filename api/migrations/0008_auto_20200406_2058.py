# Generated by Django 3.0.5 on 2020-04-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200406_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='launch_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='social_share_last_update',
            field=models.TextField(),
        ),
    ]
