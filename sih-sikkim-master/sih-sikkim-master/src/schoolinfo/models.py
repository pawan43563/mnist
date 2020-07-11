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

affi_board_school=(('CBSE',('CBSE')),('State Board',('State Board')),('ICSE',('ICSE')),
('International Board',('International Board')),('Others',('Others')),
    ('Both CBSE & State Board',('Both CBSE & State Board')))

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

    #1.28

    #1.29

    sp_pre_vocational_course=models.CharField(max_length=10,blank=True,choices=yn,verbose_name='Does the school offer any pre-vocational course(s) at the Upper-Primary stage?')
    sp_counseling=models.CharField(max_length=10,blank=True,choices=yn,verbose_name='Does the school provide educational and vocational guidance/counseling to students?')

    #1.32 AFFILIATION NUMBER

    sp_sec_affi_board=models.CharField(max_length=28,blank=True,choices=affi_board_school,verbose_name='(a) For Secondary Sections')
    sp_sec_affi_board_number=models.CharField(max_length=28,blank=True,verbose_name='Affiliation Number')
    sp_others_sec_affi_board=models.CharField(max_length=28,blank=True,verbose_name='If others,then name of the board')
    sp_high_sec_affi_board=models.CharField(max_length=28,blank=True,choices=affi_board_school,verbose_name='(b) For Higher Secondary Sections')
    sp_high_sec_affi_board_number=models.CharField(max_length=28,blank=True,verbose_name='Affiliation Number')
    sp_others_high_sec_affi_board=models.CharField(max_length=28,blank=True,verbose_name=' If others,then name of the board')


    sp_distance_primary=models.CharField(max_length=20,blank=True,verbose_name='(a) From Primary school/section')
    sp_distance_upper_primary=models.CharField(max_length=20,blank=True,verbose_name='(b) From Upper Primary school/section')
    sp_distance_secondary=models.CharField(max_length=20,blank=True,verbose_name='(c) From Secondary school/section')
    sp_distance_higher_secondary=models.CharField(max_length=20,blank=True,verbose_name='(d) From Higher Secondary school/Junior College')
    sp_all_weather_road=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='Whether school is approachable by all-weather road?')
    sp_pre_primary=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='Whether pre-primary section(other than Anganwadi) attached to school?')

    #1.35 (a)

    sp_anganwadi=models.CharField(max_length=20,blank=True,choices=yn,verbose_name="If yes,")    
    sp_anganwadi_code=models.CharField(max_length=20,blank=True,verbose_name='(a)Code of the Anganwadi Centre')
    sp_anganwadi_children=models.CharField(max_length=20,blank=True,verbose_name='(b)Total Children in Anganwadi Centre')
    sp_anganwadi_worker=models.CharField(max_length=20,blank=True,choices=yn,verbose_name='(c)Is the Anaganwadi worker trained in early childhood education')
    
    sp_pre_primary_ins_days=models.CharField(max_length=5,blank=True,verbose_name='(a) Pre-primary')
    sp_primary_ins_days=models.CharField(max_length=5,blank=True,verbose_name='(b) Primary')
    sp_upper_primary_ins_days=models.CharField(max_length=5,blank=True,verbose_name='(c) Upper primary')
    sp_secondary_ins_days=models.CharField(max_length=5,blank=True,verbose_name='(d) Secondary')
    sp_higher_secondary_ins_days=models.CharField(max_length=5,blank=True,verbose_name='(e) Higher Secondary')

    sp_pre_primary_avg_chil_days=models.CharField(max_length=5,blank=True,verbose_name='(a) Pre-primary')
    sp_primary_avg_chil_days=models.CharField(max_length=5,blank=True,verbose_name='(b) Primary')
    sp_upper_primary_avg_chil_days=models.CharField(max_length=5,blank=True,verbose_name='(c) Upper primary')
    sp_secondary_avg_chil_days=models.CharField(max_length=5,blank=True,verbose_name='(d) Secondary')
    sp_higher_secondary_avg_chil_days=models.CharField(max_length=5,blank=True,verbose_name='(e) Higher Secondary')

    sp_pre_primary_avg_teach_days=models.CharField(max_length=8,blank=True,verbose_name='(a) Pre-primary')
    sp_primary_avg_teach_days=models.CharField(max_length=8,blank=True,verbose_name='(b) Primary')
    sp_upper_primary_avg_teach_days=models.CharField(max_length=8,blank=True,verbose_name='(c) Upper primary')
    sp_secondary_avg_teach_days=models.CharField(max_length=8,blank=True,verbose_name='(d) Secondary')
    sp_higher_secondary_avg_teach_days=models.CharField(max_length=8,blank=True,verbose_name='(e) Higher Secondary')

    sp_cce_pri=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='(a) Primary')
    sp_cce_upper_pri=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='(b) Upper Primary')
    sp_cce_sec=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='(c) Secondary')
    sp_cce_higher_sec=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='(d) Higher Secondary')
    sp_rec_maintained=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='(a) Are cumulative records of pupil being maintained?')
    sp_rec_shared=models.CharField(max_length=8,blank=True,choices=yn,verbose_name='(b) Are cumulative records of pupil being shared with parents?')
    
    #1.42(a)

    #1.42(b)



    def __str__(self):
        return self.sp_school_name


status_of_building=(('Private',('Private')),
            ('Rented',('Rented')),
            ('Government',('Government')),
            ('Government School in a rent free building',('Government School in a rent free building')),
            ('No Building',('No Building')),
            ('Building',('Building')),
            ('Under Construction',('Under Construction')),
            ('School running in other Department Building',('School running in other Department Building')))

type_boundary_wall=(('Pucca',('Pucca')),('Pucca but broken',('Pucca but broken')),('Barbed wire fencing',('Barbed wire fencing')),
('Hedges',('Hedges')),('boundary walls',('boundary walls')),('others',('others')),('Partial',('Partial')),('Under Construction',('Under Construction')))

ynp=(
        ('Yes',('Yes')),('No',('No')),('Yes, but not functional',('Yes, but not functional'))
        )

de_worming=(('Complete(two doses)',('Complete(two doses)')),('Partially(one dose)',('Partially(one dose)')),('Not given',('Not given')))

special_educator=(('Dedicated',('Dedicated')),('At cluster level',('At cluster level')),('No',('No')))

dustbins_class=(('Yes and all',('Yes and all')),('No',('No')),('Yes but some',('Yes but some')))

which_comp_lab=(('ICT',('ICT')),('CAL',('CAL')),('Both',('Both')),('None',('None')))

ict_model=(('BOOT Model',('BOOT Model')),('BOO Model',('BOO Model')),('Other',('Other')))

ict_instructor=(('Full time',('Full time')),('Part Time',('Part Time')),('Not Available',('Not Available')))

class PhysicalFacilities(TimeStampMixin):
    pf_school = models.OneToOneField(School, on_delete=models.CASCADE)
    pf_status=models.CharField(max_length=50,choices=status_of_building, blank=True,verbose_name='Status of the School building')
    
    #2.2

    pf_boundary_type=models.CharField(max_length=50,choices=type_boundary_wall, blank=True,verbose_name='Type of boundary wall')
    pf_classrooms_instructional=models.CharField(max_length=50, blank=True,verbose_name='(a1) No. of Classrooms used for instructional purposes')
    pf_classrooms_construction=models.CharField(max_length=50, blank=True,verbose_name='(a2) No. of Classrooms under construction')
    pf_dilapidated=models.CharField(max_length=50, blank=True,verbose_name='(a3) Total Classrooms in dilapidated condition')
    pf_classrooms_instructional_pre_pri=models.CharField(max_length=10,blank=True,verbose_name='Pre-primary')
    pf_classrooms_instructional_pri=models.CharField(max_length=10,blank=True,verbose_name='Primary')
    pf_classrooms_instructional_upper_pri=models.CharField(max_length=10,blank=True,verbose_name='Upper primary')
    pf_classrooms_instructional_sec=models.CharField(max_length=10,blank=True,verbose_name='Secondary')
    pf_classrooms_instructional_higher_sec=models.CharField(max_length=10,blank=True,verbose_name='Higher Secondary')
    pf_classrooms_available=models.CharField(max_length=10,blank=True,verbose_name='(b) Total number of rooms other than classrooms available in School:')

    #2.3(c)

    pf_land_available=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Whether land is available for expansion of school facilities')
    pf_separate_head_available=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Whether separate room for Head Teacher/Principle available')
    pf_schools_toilet=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Does the school have toilet?')

    #2.7(a)

    pf_water_available=models.CharField(max_length=10,blank=True,verbose_name='(a) How many have running water available in the toilet/urinal for flushing and cleaning?')
    pf_hand_soap_available=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(b) Is hand washing facility with soap available near toilets/urinals block?')
    pf_incinerator_girls=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(c) Whether incinerator is available in/attached to girls toilet?')
    
    pf_drinking_water_available=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Whether drinking water is available in the school premises?')

    #2.8(a)

    pf_purifier_available=models.CharField(max_length=25,choices=ynp,blank=True,verbose_name='Whether water purifier/RO is available in the school?')
    pf_water_testing=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Whether water quality is tested from water testing lab?')
    pf_rain_harvesting=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Does the school have provision for rain water harvesting')
    pf_hand_washing_available=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Whether hand washing facility with soap available')
    pf_rain_harvesting=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Does the school have provision for rain water harvesting?')
    pf_hand_washing_available=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Whether hand washing facility with soap available for available for washing hands before and after meal?')
    pf_number_hand_washing=models.CharField(max_length=10,blank=True,verbose_name='(a) Number of wash points')
    pf_electricity_connection=models.CharField(max_length=30,choices=ynp,blank=True,verbose_name='Whether electricity connection is available in the school ?')
    pf_solar_panel=models.CharField(max_length=30,choices=ynp,blank=True,verbose_name='Whether solar panel available in school?')

    #2.12(a)

    pf_librarian=models.CharField(max_length=10,choices=yn,blank=True,verbose_name=' Does the school have a full-time librarian?')
    pf_magazine=models.CharField(max_length=10,choices=yn,blank=True,verbose_name=' Does the School subsribe to newspapers/magazines?')

    pf_playground_facility=models.CharField(max_length=28,choices=yn,blank=True,verbose_name='Whether Playground facility is available?')
    pf_other_arrangement=models.CharField(max_length=28,choices=yn,blank=True,verbose_name='(a) if no, whether school has made adequate arrangements for children to play outdoor games and other physical activities in an adjoining playground/municipal park etc.')
    
    pf_medical_check_up=models.CharField(max_length=20,choices=yn,blank=True,verbose_name='Whether Medical check-up is conducted(last year)?')
    pf_total_medical_check_ups=models.CharField(max_length=10,blank=True,verbose_name='(a)Total Number of  Medical check-ups is conducted(last year)?')
    
    pf_de_worming_given=models.CharField(max_length=20,choices=de_worming,blank=True,verbose_name='(b)De-worming tablets given to children?')
    pf_iron_folic=models.CharField(max_length=20,choices=yn,blank=True,verbose_name='(c)Iron and Folic acid tablets given to children')

    pf_ramp_disabled=models.CharField(max_length=20,choices=yn,blank=True,verbose_name='Whether ramp for disabled children to access school building exists?')
    pf_hand_rails=models.CharField(max_length=20,choices=yn,blank=True,verbose_name='(a) If yes,whether Hand-rails for ramp is available?')
    
    pf_school_special_edu=models.CharField(max_length=20,choices=special_educator,blank=True,verbose_name='Whether School has special educator?')
    pf_kitchen_garden=models.CharField(max_length=20,choices=yn,blank=True,verbose_name='Whether Kitchen Garden is available in school?')

    
    pf_dustbins_class=models.CharField(max_length=41,choices=dustbins_class,blank=True,verbose_name='(a) Class room')
    pf_dustbins_toilet=models.CharField(max_length=41,choices=yn,blank=True,verbose_name='(b) Toilet')
    pf_dustbins_kitchen=models.CharField(max_length=41,choices=yn,blank=True,verbose_name='(c) kitchen')
    pf_students_furniture=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='No. of Students for whom furniture is available?')

    pf_sep_room_head_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(a) Separate Room for Assistant Head Teacher/Vice principal')
    pf_sep_girls_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(b) Separate common room for girls')
    pf_staff_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(c) Staffroom for teachers')
    pf_arts_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(d) Co-curricular activity room/arts and crafts room')
    pf_staff_quarters_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(e) Staff quarters(including residential quarters for Head Teacher/Principal and Asst. Head Teacher/Vice Principal)')
    pf_science_lab_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(f) Integrated Science laboratory(integrated laboratory is the one in which Physics,Chemistry and Biology practical are held)for Secondary sections only')
    pf_lib_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(g) Library room')
    pf_comp_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(h) Computer room')
    pf_tinkering_sec=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='(i) Tinkering Lab')

    #2.21

    pf_equip_audio=models.CharField(max_length=100,choices=ynp,blank=True,verbose_name='(a) Audio/Visual/Public Address System')
    pf_equip_sci_kit=models.CharField(max_length=100,choices=ynp,blank=True,verbose_name='(b) Science Kit')
    pf_equip_math_kit=models.CharField(max_length=100,choices=ynp,blank=True,verbose_name='(c) Math kit')
    pf_equip_biometric=models.CharField(max_length=100,choices=ynp,blank=True,verbose_name='(d) Biometric device')

    
    pf_which_comp_lab=models.CharField(max_length=100,choices=which_comp_lab,blank=True,verbose_name='Which Computer lab is available in the School?')
    pf_ict_year=models.CharField(max_length=100,blank=True,verbose_name='(a)Year of implementation')
    pf_ict_functional=models.CharField(max_length=100,choices=yn,blank=True,verbose_name='(b)Whether ICT lab is functional or not?')

    
    pf_ict_model=models.CharField(max_length=100,choices=ict_model,blank=True,verbose_name='(c)Which Model is implemented in the School?')
    
    
    pf_ict_instructor=models.CharField(max_length=100,choices=ict_instructor,blank=True,verbose_name='(d)Type of ICT instructor in the School?')

    #2.32

    pf_ict_for_teaching=models.CharField(max_length=10,choices=yn,blank=True,verbose_name='Whether ICT based tools are used for teaching?')
    pf_ict_for_teaching_hours=models.CharField(max_length=10,blank=True,verbose_name='(a) If yes, Number of Hours spent per week')

    def __str__(self):
        return self.sp_school_name
