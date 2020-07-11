# Generated by Django 3.0.8 on 2020-07-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolinfo', '0010_auto_20200711_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_repondent_contact_no',
            field=models.CharField(blank=True, max_length=18, verbose_name='(c)Respondent Contact No.'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_respondent_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='(b)Respondent Name(In Capital Letters)'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_school_email',
            field=models.CharField(blank=True, max_length=20, verbose_name='(d)Email Of School'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_school_website',
            field=models.CharField(blank=True, max_length=25, verbose_name='(e)Website Of School'),
        ),
    ]
