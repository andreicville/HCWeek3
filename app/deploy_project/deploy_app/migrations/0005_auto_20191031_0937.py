# Generated by Django 2.2.6 on 2019-10-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_app', '0004_auto_20191031_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brands',
            name='title',
        ),
        migrations.AddField(
            model_name='brands',
            name='title',
            field=models.CharField(default='Brand Title Default', max_length=50),
        ),
    ]
