# Generated by Django 3.2 on 2021-05-03 11:56

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Age')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Actors and Directors',
                'verbose_name_plural': 'Actors and Directors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=150)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genre',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Tagline')),
                ('description', models.TextField(verbose_name='Description')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2021, verbose_name='Date Released')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('budget', models.PositiveIntegerField(default=0, verbose_name='Budget')),
                ('fees', models.PositiveIntegerField(default=0, verbose_name='Fees')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='actors')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Category')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='directors')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='genres')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Rating star',
                'verbose_name_plural': 'Rating stars',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('text', models.TextField(max_length=5000, verbose_name='Message')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.review', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP adress')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='film')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='star')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Image')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Film')),
            ],
            options={
                'verbose_name': 'Movie shot',
                'verbose_name_plural': 'Movie shots',
            },
        ),
    ]
