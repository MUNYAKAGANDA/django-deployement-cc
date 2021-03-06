# Generated by Django 2.0.5 on 2018-08-01 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20180730_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('slug', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=7000)),
                ('date_happen', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='card_no',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='email',
            field=models.CharField(default='email @example.com', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='key',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='phone_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trainer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='training',
            name='description',
            field=models.CharField(max_length=7000, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='thumb',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='company_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
