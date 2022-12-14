# Generated by Django 4.0.6 on 2022-09-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_alter_prospect_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterinfo',
            name='followers_count',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='following_count',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='last_tweet',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='location',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='profile_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='retweets_count',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='tweets_count',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='username',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
