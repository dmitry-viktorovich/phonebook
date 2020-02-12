# Generated by Django 3.0.2 on 2020-02-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0004_auto_20200212_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Имя',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Должность',
        ),
        migrations.AddField(
            model_name='person',
            name='department_position',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='department',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='extension_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
