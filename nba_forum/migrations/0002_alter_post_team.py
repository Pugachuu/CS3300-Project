# Generated by Django 4.2.7 on 2023-11-05 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nba_forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='team',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='nba_forum.team'),
        ),
    ]
