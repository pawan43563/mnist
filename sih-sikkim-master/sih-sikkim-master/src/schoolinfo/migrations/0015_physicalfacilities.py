# Generated by Django 3.0.8 on 2020-07-11 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('schoolinfo', '0014_auto_20200711_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalFacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academic_year', models.CharField(blank=True, max_length=50)),
                ('pf_status', models.CharField(blank=True, choices=[('Private', 'Private'), ('Rented', 'Rented'), ('Government', 'Government'), ('Government School in a rent free building', 'Government School in a rent free building'), ('No Building', 'No Building'), ('Building', 'Building'), ('Under Construction', 'Under Construction'), ('School running in other Department Building', 'School running in other Department Building')], max_length=50, verbose_name='Status of the School building')),
                ('sp_school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.School')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
