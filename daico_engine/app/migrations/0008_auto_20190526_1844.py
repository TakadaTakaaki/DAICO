# Generated by Django 2.1 on 2019-05-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190526_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pr', models.CharField(max_length=70)),
                ('tell', models.CharField(max_length=12)),
                ('price', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=10)),
                ('credit', models.CharField(max_length=50)),
                ('homepage', models.URLField(max_length=100)),
                ('staff', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=20)),
                ('service', models.TextField()),
                ('pay', models.TextField()),
                ('cancel', models.TextField()),
                ('security', models.TextField()),
            ],
            options={
                'db_table': 'company_data',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_plan', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=75)),
                ('price', models.CharField(max_length=30)),
                ('terms', models.CharField(max_length=20)),
                ('effect', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'plan',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('A', '男性'), ('C', 'その他'), ('B', '女性')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('B', 'Customer User'), ('A', 'Client User')], default='B', max_length=1),
        ),
    ]
