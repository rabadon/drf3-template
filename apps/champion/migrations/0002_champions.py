# Generated by Django 2.0.4 on 2018-10-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='チャンピオン名')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': 'チャンピオンマスター',
                'db_table': 'm_champions',
                'ordering': ['id'],
            },
        ),
    ]
