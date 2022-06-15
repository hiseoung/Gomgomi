# Generated by Django 3.2.7 on 2022-05-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_life_quotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='voice_chat_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('context', models.CharField(blank=True, max_length=200, null=True)),
                ('voice', models.FileField(upload_to='voice_chat/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('chat_flag', models.CharField(blank=True, max_length=10, null=True)),
                ('conversation_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'voice_chat_info',
                'ordering': ['created'],
            },
        ),
        migrations.AlterField(
            model_name='chat_info',
            name='chat_flag',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='chat_info',
            name='context',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chat_info',
            name='conversation_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chat_info',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]