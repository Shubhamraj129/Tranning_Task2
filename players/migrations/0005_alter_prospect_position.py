# Generated by Django 4.0.6 on 2022-09-01 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_alter_prospect_offer_alter_prospect_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='players.position'),
        ),
    ]