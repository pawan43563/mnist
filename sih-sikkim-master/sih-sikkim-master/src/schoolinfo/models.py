from django.db import models
from profiles.models import School

school_located_choices = (('Rural', 'Rural'), ('Urban', 'Urban'))

class TimeStampMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    academic_year = models.CharField(max_length=50, blank=True)

    class Meta:
        abstract = True

yn=(
        ('Yes',('Yes')),('No',('No'))
        )

school_category_code=(
    ('Primary only with grades 1 to 5',('Primary only with grades 1 to 5')),
    ('Primary only with grades 1 to 8',('Primary only with grades 1 to 8')),
    ('Higher Secondary with grades 1 to 12',('Higher Secondary with grades 1 to 12')),
    ('Upper Primary only with grades 6 to 8',('Upper Primary only with grades 6 to 8')),
    ('Higher Secondary with grades 6 to 12',('Higher Secondary with grades 6 to 12')),
    ('Secondary/Sr.Sec. with grades 1 to 10',('Secondary/Sr.Sec. with grades 1 to 10')),
    ('Secondary/Sr.Sec. with grades 6 to 10',('Secondary/Sr.Sec. with grades 6 to 10')),
    ('Secondary/Sr.Sec. with grades 9 and 10',('Secondary/Sr.Sec. with grades 9 and 10')),
    ('Higher Secondary with grades 9 to 12',('Higher Secondary with grades 9 to 12')),
    ('Hr.Sec. /Jr.College only with grades 11 and 12',('Hr.Sec. /Jr.College only with grades 11 and 12'))
)   

type_of_school=(
    ('Boys',('Boys')),
    ('Girls',('Girls')),
    ('Co-educational',('Co-educational'))
)

management_school_code=(
    ('Department of Education',('Department of Education')),
    ('Tribal Welfare Department',('Tribal Welfare Department')),
    ('Local Body',('Local Body')),
    ('Government Aided',('Government Aided')),
    ('Private Unaided(Recognized)',('Private Unaided(Recognized)')),
    ('Other Govt. managed schools',('Other Govt. managed schools')),
    ('Unrecognized',('Unrecognized')),
    ('Social Welfare Department',('Social Welfare Department')),
    ('Ministry of Labour',('Ministry of Labour')),
    ('Kendriya Vidyalaya / Central School',('Kendriya Vidyalaya / Central School')),
    ('Jawahar Navodaya Vidyalaya',('Jawahar Navodaya Vidyalaya')),
    ('Sainik School',('Sainik School')),
    ('RailwaySchool',('RailwaySchool')),
    ('Central Tibetan School',('Central Tibetan School')),
    ('Madarsa Recognized(by Wakf board/Madarsa Board)',('Madarsa Recognized(by Wakf board/Madarsa Board)')),
    ('Madarsa Unrecoginzed',('Madarsa Unrecoginzed')),    
)

residential_type=(
        ('Ashram(Govt.)',('Ashram(Govt.)')),
        ('Non-ashram(Govt.)',('Non-ashram(Govt.)')),
        ('Private',('Private')),
        ('Others',('Others')),
        ('KGBV',('KGBV')),
        ('Model School',('Model School')),
        ('Eklavya Model',('Eklavya Model')),
    )

minority_type=(
        ('Muslim',('Muslim')),
        ('Sikh',('Sikh')),
        ('Jain',('Jain')),
        ('Christian',('Christian')),
        ('Parsi',('Parsi')),
        ('Buddhist',('Buddhist')),
        ('Any other',('Any other')),
        ('Linguistic Minority',('Linguistic Minority'))
    )

class SchoolProfile(TimeStampMixin):
    sp_school = models.OneToOneField(School, on_delete=models.CASCADE)
    sp_school_name = models.CharField(max_length=250, verbose_name='School Name (In Capital Letters)')
    sp_school_located = models.CharField(max_length=50, choices=school_located_choices, blank=True, verbose_name='Is the school located in Rural or Urban Area')
    sp_village_ward = models.CharField(max_length=250, blank=True, verbose_name='Village Name(for rural area)/Ward Number(for urban area)')
    sp_habitation_mohalla=models.CharField(max_length=250, blank=True,verbose_name='Habitation name(for rural area)/Ward Number(for urban area)')
    sp_pincode=models.CharField(null=True,max_length=6,blank=True,verbose_name='Pin Code')
    sp_gram_panchayat=models.CharField(max_length=30,blank=True,verbose_name='Name of the Gram Panchayat(for rurul area only)')
    sp_crc=models.CharField(max_length=20,blank=True,verbose_name='Name of the Cluster Resource Centre(CRC)')
    sp_cd=models.CharField(max_length=30,blank=True,verbose_name='Name of Community Development(CD)Block/Mandal/Taluka')
    sp_ed=models.CharField(max_length=30,blank=True,verbose_name='Name of the Educational Block')
    sp_assembly=models.CharField(max_length=30,blank=True,verbose_name='Name of the Assembly Constituency')
    sp_parliamentary=models.CharField(max_length=30,blank=True,verbose_name='Name of the Parliamentary Constituency')
    sp_ed=models.CharField(max_length=30,blank=True,verbose_name='Name of the Educational Block')
    sp_municipality=models.CharField(max_length=30,blank=True,verbose_name='Name of the Municipality(where applicable)')
    sp_city_name=models.CharField(max_length=30,blank=True,verbose_name='Name of the city(where applicable)')

    #1.14(a)

    sp_respondent_name=models.CharField(max_length=30,blank=True,verbose_name='(b)Respondent Name(In Capital Letters)')
    sp_repondent_contact_no=models.CharField(max_length=18,blank=True,verbose_name='(c)Respondent Contact No.')
    sp_school_email=models.CharField(max_length=20,blank=True,verbose_name='(d)Email Of School')
    sp_school_website=models.CharField(max_length=25,blank=True,verbose_name='(e)Website Of School')
    sp_school_category=models.CharField(max_length=50,choices=school_category_code,blank=True,verbose_name='School Category')

    sp_lowest_class=models.CharField(max_length=10,blank=True,verbose_name='(a)Lowest Class in the School ')
    sp_highest_class=models.CharField(max_length=10,blank=True,verbose_name='(b)Highest Class in the School ')
    sp_school_type=models.CharField(max_length=15,choices=type_of_school,blank=True,verbose_name='Type of School')

    #1.18

    sp_management_code=models.CharField(max_length=50,choices=management_school_code,blank=True,verbose_name='Management of the school')
    sp_establishment_year = models.CharField(max_length=10,blank=True,verbose_name='Year of establishment of School')
    sp_primary_year = models.CharField(max_length=10,blank=True,verbose_name='(a)Primary')
    sp_upper_primary_year = models.CharField(max_length=10,blank=True,verbose_name='(b)Upper Primary')
    sp_secondary_year = models.CharField(max_length=10,blank=True,verbose_name='(c)Secondary')
    sp_higher_secondary_year = models.CharField(max_length=10,blank=True,verbose_name='(d)Higher Secondary')
    sp_pri_to_upper_pri_year = models.CharField(max_length=50,blank=True,verbose_name='(a)Primary to Upper Primary')
    sp_upper_pri_to_sec_year = models.CharField(max_length=50,blank=True,verbose_name='(b)Upper Primary to Secondary')
    sp_sec_to_upper_sec_year = models.CharField(max_length=50,blank=True,verbose_name='(c)Secondary to Higher Secondary')
    sp_is_cwsn=models.CharField(max_length=50,blank=True,choices=yn,verbose_name='Is this a special school for CWSN?')
    sp_is_shift=models.CharField(max_length=50,blank=True,choices=yn,verbose_name='Is this a shift school?')
    sp_is_residential=models.CharField(max_length=50,blank=True,choices=yn,verbose_name='Is this a residential school?')
    sp_residential_type=models.CharField(max_length=50,blank=True,choices=residential_type,verbose_name='(a)If Yes, Type of residential school')

    #1.25 (b)

    sp_minority=models.CharField(max_length=10,blank=True,choices=yn,verbose_name='Is this a minority managed school?')
    sp_minority_type=models.CharField(max_length=30,blank=True,choices=minority_type,verbose_name='(a)If yes, Type of minority community managing the school')
    sp_majority=models.CharField(max_length=10,blank=True,choices=yn,verbose_name='Are majority of the pupils taught through their mother tongure at the primary level?')


    def __str__(self):
        return self.sp_school_name