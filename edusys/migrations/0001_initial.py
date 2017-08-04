# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Cno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Cname', models.CharField(max_length=20)),
                ('Classhour', models.IntegerField()),
                ('Credit', models.FloatField()),
                ('TimeTable', models.CharField(max_length=15)),
                ('Place', models.CharField(max_length=20)),
                ('Limit_Stu', models.IntegerField()),
                ('Exist_Stu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Score', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edusys.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Sno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=20)),
                ('Spassword', models.CharField(max_length=15)),
                ('Semail', models.EmailField(max_length=254)),
                ('Ssex', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('Tno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Tname', models.CharField(max_length=20)),
                ('Tsex', models.CharField(max_length=2)),
                ('Tpassword', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edusys.Student'),
        ),
        migrations.AddField(
            model_name='report',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edusys.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edusys.Teacher'),
        ),
    ]
