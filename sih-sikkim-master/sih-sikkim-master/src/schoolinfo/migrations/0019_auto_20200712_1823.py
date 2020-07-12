# Generated by Django 3.0.8 on 2020-07-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolinfo', '0018_auto_20200711_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_ac_constituted',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(e) Whether the school has constitued its Academic Committee(AC)?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_academic_start',
            field=models.CharField(blank=True, max_length=20, verbose_name='When does the academic session start? Give the month:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_account_name_smc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Account in the Name of:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_account_name_smdc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Account in the Name of:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_account_number_smc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Account Number:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_account_number_smdc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Account Number:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_bank_branch_smc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Branch:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_bank_branch_smdc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Branch:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_bank_name_smc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Bank Name:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_bank_name_smdc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Bank Name:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_brc_visits',
            field=models.CharField(blank=True, max_length=8, verbose_name='(c)No. of visits by Block Level Officers(BRC/BEO):'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_children_rte_current',
            field=models.CharField(blank=True, max_length=9, verbose_name='(a)No. of children enrolled at entry level under Section 12 of the RTE Act in current academic year:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_children_rte_prev',
            field=models.CharField(blank=True, max_length=9, verbose_name='(b)No. of children enrolled at entry level under Section 12 of the RTE Act in current previous years:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_crc_visits',
            field=models.CharField(blank=True, max_length=8, verbose_name='(b)No. of visits by CRC Co-ordinator:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_graded_received',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Whether the School has received graded supplementary material in previous academic year?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_ifsc_smc',
            field=models.CharField(blank=True, max_length=20, verbose_name='IFSC Code:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_ifsc_smdc',
            field=models.CharField(blank=True, max_length=20, verbose_name='IFSC Code:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_no_of_meetings_smc',
            field=models.CharField(blank=True, max_length=8, verbose_name='(f)Number of meetings held by SMC(previous year):'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_no_of_meetings_smc_last',
            field=models.CharField(blank=True, max_length=8, verbose_name='(a)Number of SMDC meetings held during the last academic year?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_no_of_members_training',
            field=models.CharField(blank=True, max_length=8, verbose_name='(e)Number of members provided training:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_no_of_parents',
            field=models.CharField(blank=True, max_length=8, verbose_name='(b) Number of parents/guardians:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_no_of_teachers',
            field=models.CharField(blank=True, max_length=8, verbose_name='(d)Number of teachers'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_nominees_local',
            field=models.CharField(blank=True, max_length=8, verbose_name='(c)Number of Representatives/nominees from local authority/local/government/urban local body:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_officers_visits',
            field=models.CharField(blank=True, max_length=8, verbose_name='(d)No. of visits by District/State Level Officers:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_pta_constituted',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(f) Whether the school has constitued its Parent-Teacher Association(PTA)?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_pta_meetings_last',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='1. Number of PTA meetings held during last year'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_remedial_teaching',
            field=models.CharField(blank=True, max_length=50, verbose_name='No. of Students attending Remedial Teaching in current year:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_sbc_constituted',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(d) Whether School Building Committee(SBC) has been constituted?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_school_visits',
            field=models.CharField(blank=True, max_length=8, verbose_name='(a)No. of academic inspections:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_separate_bank_smc',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(h)Whether separate bank account for SMC is being maintained?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_separate_bank_smdc',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(c)Whether separate bank account for SMDC is being maintained?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_smc_consulted',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Whether School Management Committee(SMC) has been constituted?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_smc_members',
            field=models.CharField(blank=True, max_length=8, verbose_name='(a) Total number of members in SMC:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_smc_prepared_plan',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(g)Whether SMC has prepared the School Development Plan?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_smc_smdc_constituted',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(a)Whether School Management and Development Committee has been constituted?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_smc_smdc_same',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='Whether School Management Committee(SMC) and School Management and Development Committee(SMDC)are same in the school?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_smdc_prepared_plan',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=8, verbose_name='(b)Whether SMDC has prepared School Improvement Plan?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_special_training',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Whether an out of School Shildren enrolled in the school are attending Special Training?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_special_training_com_previous',
            field=models.CharField(blank=True, max_length=10, verbose_name='(c) No. of children completed Special Training in previous academic year:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_special_training_current',
            field=models.CharField(blank=True, max_length=10, verbose_name='(a) No. of children enrolled for Special Training in current year:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_special_training_previous',
            field=models.CharField(blank=True, max_length=10, verbose_name='(b) No. of children enrolled for Special Training in previous academic year:'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_textbook_received',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Whether full set of textbooks received in current academic year?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_textbook_received_year',
            field=models.CharField(blank=True, max_length=50, verbose_name='If yes, When were the text books received in current academic year?(Month)'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_training_type',
            field=models.CharField(blank=True, choices=[('Residential', 'Residential'), ('non-residential', 'non-residential'), ('both', 'both')], max_length=200, verbose_name='(f) Type of Training being conducted?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_where_conducted_training',
            field=models.CharField(blank=True, choices=[('School premises', 'School premises'), ('other school premises', 'other school premises'), ('both 1&2', 'both 1&2')], max_length=200, verbose_name='(e) Where is Special Training conducted?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sp_who_conducts_training',
            field=models.CharField(blank=True, choices=[('School teachers', 'School teachers'), ('specially engaged teachers', 'specially engaged teachers'), ('both 1&2', 'both 1&2'), ('NGO', 'NGO'), ('Others', 'Others')], max_length=200, verbose_name='(d) Who conducts Special Training?'),
        ),
    ]
