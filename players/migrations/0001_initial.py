# Generated by Django 4.0.6 on 2022-08-28 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=15)),
                ('weight', models.CharField(max_length=15)),
                ('image', models.URLField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.city')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.offers')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.position')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.highschool')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TwitterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('tweets_count', models.CharField(max_length=30, null=True)),
                ('followers_count', models.CharField(max_length=30, null=True)),
                ('following_count', models.CharField(max_length=30, null=True)),
                ('last_tweet', models.CharField(max_length=30, null=True)),
                ('retweets_count', models.CharField(max_length=30, null=True)),
                ('profile_name', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.prospect')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.country')),
            ],
        ),
        migrations.AddField(
            model_name='prospect',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.year'),
        ),
        migrations.AddField(
            model_name='offers',
            name='teams',
            field=models.ManyToManyField(to='players.team'),
        ),
        migrations.CreateModel(
            name='HardCommited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commited', models.CharField(max_length=20, null=True)),
                ('requited_by', models.CharField(max_length=40, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.prospect')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.team')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.state'),
        ),
    ]
