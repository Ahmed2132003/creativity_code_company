# Generated by Django 5.0.4 on 2024-11-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('client_name', models.CharField(max_length=255)),
                ('developer_name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='portfolio_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='portfolio_videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]