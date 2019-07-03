# Generated by Django 2.2.2 on 2019-07-02 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(verbose_name='图片编号')),
                ('like_num', models.IntegerField(default=0, verbose_name='喜欢数量')),
            ],
        ),
        migrations.CreateModel(
            name='Per',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='PerLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jk.Img', verbose_name='图片')),
                ('per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jk.Per', verbose_name='用户')),
            ],
        ),
    ]
