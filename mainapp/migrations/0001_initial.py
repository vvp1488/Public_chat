# Generated by Django 3.2.8 on 2021-10-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('email', models.EmailField(max_length=254, verbose_name='Електронная почта')),
                ('text', models.TextField(max_length=100, verbose_name='Текст сообщения')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
