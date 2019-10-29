# Generated by Django 2.2.6 on 2019-10-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('accessory_type', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('bike_model', models.ManyToManyField(to='deploy_app.Bikes')),
                ('part_model', models.ManyToManyField(to='deploy_app.Parts')),
            ],
        ),
        migrations.DeleteModel(
            name='Accesories',
        ),
    ]
