# Generated by Django 3.0.4 on 2020-07-02 20:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Name', models.CharField(max_length=35, unique=True)),
                ('Movie_Description', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Director', models.CharField(blank=True, max_length=35)),
                ('Movie', models.ManyToManyField(blank=True, related_name='Movie_Director', to='api.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_CHARACTER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Character', models.CharField(blank=True, max_length=20)),
                ('Movie', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Movie_CHARACTER', to='api.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Ratings', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Movie_Ratings', to='api.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'movie')},
                'index_together': {('user', 'movie')},
            },
        ),
    ]
