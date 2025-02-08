# Generated by Django 5.1.5 on 2025-02-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_delete_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='subscriptions', to='news.category')),
            ],
        ),
    ]
