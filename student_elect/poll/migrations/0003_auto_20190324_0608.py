# Generated by Django 2.1.7 on 2019-03-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20190324_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='round',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='imagefile',
            field=models.ImageField(default='default.png', upload_to='candidates'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.TextField(choices=[('Active', 'A'), ('Inactive', 'I')], default='A'),
        ),
    ]
