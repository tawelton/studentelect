# Generated by Django 2.1.7 on 2019-03-30 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_auto_20190330_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Poll'),
        ),
    ]
