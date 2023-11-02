# Generated by Django 4.2.2 on 2023-07-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_alter_user_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=10)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('userMessage', models.CharField(max_length=1000)),
            ],
        ),
    ]
