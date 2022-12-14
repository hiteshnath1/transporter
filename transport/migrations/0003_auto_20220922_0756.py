# Generated by Django 3.1.7 on 2022-09-22 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_transport_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='email',
            field=models.CharField(default='admin@transport.com', max_length=150),
        ),
        migrations.AddField(
            model_name='branches',
            name='landline_no',
            field=models.IntegerField(default=9521446207),
        ),
        migrations.AddField(
            model_name='branches',
            name='mobile_no',
            field=models.IntegerField(default=9521446207),
        ),
        migrations.AddField(
            model_name='transport',
            name='email',
            field=models.CharField(default='admin@transport.com', max_length=150),
        ),
        migrations.AddField(
            model_name='transport',
            name='landline_no',
            field=models.IntegerField(default=9521446207),
        ),
        migrations.AddField(
            model_name='transport',
            name='mobile_no',
            field=models.IntegerField(default=9521446207),
        ),
    ]
