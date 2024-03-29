# Generated by Django 4.2.1 on 2024-02-17 00:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='BioRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(geography=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ConservationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.SmallIntegerField()),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Realm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubRealm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('realm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subrealms', to='ecodata.realm')),
            ],
        ),
        migrations.CreateModel(
            name='EcoRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('area', models.DecimalField(decimal_places=6, max_digits=10)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(geography=True, srid=4326)),
                ('color', models.CharField(max_length=7)),
                ('description', models.TextField()),
                ('bio_region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ecoregions', to='ecodata.bioregion')),
                ('biome', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ecoregions', to='ecodata.biome')),
                ('conservation_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ecoregions', to='ecodata.conservationstatus')),
            ],
        ),
        migrations.AddField(
            model_name='bioregion',
            name='sub_realm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bioregions', to='ecodata.subrealm'),
        ),
    ]
