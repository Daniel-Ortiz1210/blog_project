# Generated by Django 4.1 on 2022-08-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('published', models.BooleanField(default=False)),
                ('miniature', models.ImageField(blank=True, upload_to='blog_centre/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='categories.category')),
            ],
        ),
    ]
