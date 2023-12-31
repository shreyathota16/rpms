# Generated by Django 4.2.3 on 2023-07-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='researchpapers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=30)),
                ('tdept', models.CharField(max_length=10)),
                ('tid', models.IntegerField()),
                ('temail', models.CharField(max_length=30)),
                ('ptitle', models.CharField(max_length=30)),
                ('pdate', models.CharField(max_length=30)),
                ('pdesc', models.CharField(max_length=100)),
                ('pnat', models.CharField(max_length=20)),
                ('ptype', models.CharField(max_length=20)),
                ('pssn', models.IntegerField()),
                ('pfield', models.CharField(max_length=30)),
                ('plink', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
