# Generated by Django 3.2.12 on 2022-03-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0050_auto_20220211_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catfolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.IntegerField()),
                ('folder_name', models.CharField(blank=True, max_length=2000)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Catlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signid', models.IntegerField()),
                ('signname', models.CharField(blank=True, max_length=2000)),
                ('projectid', models.IntegerField()),
                ('imagepath', models.CharField(blank=True, max_length=2000)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('group_image', models.CharField(blank=True, max_length=2000)),
                ('label_mode_dev', models.CharField(blank=True, max_length=2000)),
                ('label_mode_eva', models.CharField(blank=True, max_length=2000)),
                ('order', models.CharField(blank=True, max_length=2000)),
                ('folder_name', models.CharField(blank=True, max_length=2000)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signid', models.IntegerField()),
                ('signname', models.CharField(blank=True, max_length=2000)),
                ('projectid', models.IntegerField()),
                ('imagepath', models.CharField(blank=True, max_length=2000)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('group_image', models.CharField(blank=True, max_length=2000)),
                ('label_mode_dev', models.CharField(blank=True, max_length=2000)),
                ('label_mode_eva', models.CharField(blank=True, max_length=2000)),
                ('order', models.CharField(blank=True, max_length=2000)),
                ('folder_name', models.CharField(blank=True, max_length=2000)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.AlterField(
            model_name='attributespec',
            name='default_value',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='attributespec',
            name='input_type',
            field=models.CharField(choices=[('checkbox', 'CHECKBOX'), ('radio', 'RADIO'), ('number', 'NUMBER'), ('text', 'TEXT'), ('select', 'SELECT'), ('Catalogue', 'CATALOUGE')], max_length=16),
        ),
    ]
