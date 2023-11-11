# Generated by Django 2.2 on 2023-11-04 09:53

import django.core.validators
from django.db import migrations, models
import myblog.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'unique': '이미 있는 제목입니당'}, max_length=50, unique=True)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10, '10글자 이상 작성해주세요'), myblog.validators.validate_symbols])),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('dt_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
            ],
        ),
    ]