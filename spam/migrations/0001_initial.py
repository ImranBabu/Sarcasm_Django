# Generated by Django 2.0 on 2019-03-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.CharField(max_length=500)),
                ('spam', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('pwd', models.CharField(max_length=500)),
                ('mailid', models.CharField(max_length=500)),
                ('ph', models.CharField(max_length=500)),
            ],
        ),
    ]
