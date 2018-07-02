from django.db import models
#from django.contrib.auth.models import User
from django.urls import reverse
#from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.

TERM_STATUS = (
    ('FIRST TERM', 'FIRST TERM'),
    ('SECOND TERM', 'SECOND TERM'),
    ('THIRD TERM', 'THIRD TERM')
)

class Jas(models.Model):
    """
    A Class defining JAS student result records.
    """
    # Fields
    student_name = models.CharField(max_length=20, help_text="Enter Student Name")
    adm_no = models.CharField(max_length=15, help_text="Enter Student Admission Number")
    average = models.CharField(max_length=15, help_text="Average Score in Term")
    position = models.CharField(max_length=5, help_text="Student's position in Term")
    
    hausa_ca = models.CharField(max_length=2, help_text="C.A Score")
    hausa_exam = models.CharField(max_length=2, help_text="Exam Score")
    hausa_total = models.CharField(max_length=3, help_text="Total Course Score")
    hausa_grade = models.CharField(max_length=3, help_text="Grade")
    hausa_remark = models.CharField(max_length=10, help_text="Remark")

    english_ca = models.CharField(max_length=2, help_text="C.A Score")
    english_exam = models.CharField(max_length=2, help_text="Exam Score")
    english_total = models.CharField(max_length=3, help_text="Total Course Score")
    english_grade = models.CharField(max_length=3, help_text="Grade")
    english_remark = models.CharField(max_length=10, help_text="Remark")

    math_ca = models.CharField(max_length=2, help_text="C.A Score")
    math_exam = models.CharField(max_length=2, help_text="Exam Score")
    math_total = models.CharField(max_length=3, help_text="Total Course Score")
    math_grade = models.CharField(max_length=3, help_text="Grade")
    math_remark = models.CharField(max_length=10, help_text="Remark")

    arabic_ca = models.CharField(max_length=2, help_text="C.A Score")
    arabic_exam = models.CharField(max_length=2, help_text="Exam Score")
    arabic_total = models.CharField(max_length=3, help_text="Total Course Score")
    arabic_grade = models.CharField(max_length=3, help_text="Grade")
    arabic_remark = models.CharField(max_length=10, help_text="Remark")

    basic_sci_ca = models.CharField(max_length=2, help_text="C.A Score")
    basic_sci_exam = models.CharField(max_length=2, help_text="Exam Score")
    basic_sci_total = models.CharField(max_length=3, help_text="Total Course Score")
    basic_sci_grade = models.CharField(max_length=3, help_text="Grade")
    basic_sci_remark = models.CharField(max_length=10, help_text="Remark")

    civil_edu_ca = models.CharField(max_length=2, help_text="C.A Score")
    civil_edu_exam = models.CharField(max_length=2, help_text="Exam Score")
    civil_edu_total = models.CharField(max_length=3, help_text="Total Course Score")
    civil_edu_grade = models.CharField(max_length=3, help_text="Grade")
    civil_edu_remark = models.CharField(max_length=10, help_text="Remark")

    com_stu_ca = models.CharField(max_length=2, help_text="C.A Score")
    com_stu_exam = models.CharField(max_length=2, help_text="Exam Score")
    com_stu_total = models.CharField(max_length=3, help_text="Total Course Score")
    com_stu_grade = models.CharField(max_length=3, help_text="Grade")
    com_stu_remark = models.CharField(max_length=10, help_text="Remark")

    islamic_stu_ca = models.CharField(max_length=2, help_text="C.A Score")
    islamic_stu_exam = models.CharField(max_length=2, help_text="Exam Score")
    islamic_stu_total = models.CharField(max_length=3, help_text="Total Course Score")
    islamic_stu_grade = models.CharField(max_length=3, help_text="Grade")
    islamic_stu_remark = models.CharField(max_length=10, help_text="Remark")

    french_ca = models.CharField(max_length=2, help_text="C.A Score")
    french_exam = models.CharField(max_length=2, help_text="Exam Score")
    french_total = models.CharField(max_length=3, help_text="Total Course Score")
    french_grade = models.CharField(max_length=3, help_text="Grade")
    french_remark = models.CharField(max_length=10, help_text="Remark")

    basic_tech_ca = models.CharField(max_length=2, help_text="C.A Score")
    basic_tech_exam = models.CharField(max_length=2, help_text="Exam Score")
    basic_tech_total = models.CharField(max_length=3, help_text="Total Course Score")
    basic_tech_grade = models.CharField(max_length=3, help_text="Grade")
    basic_tech_remark = models.CharField(max_length=10, help_text="Remark")

    social_stu_ca = models.CharField(max_length=2, help_text="C.A Score")
    social_stu_exam = models.CharField(max_length=2, help_text="Exam Score")
    social_stu_total = models.CharField(max_length=3, help_text="Total Course Score")
    social_stu_grade = models.CharField(max_length=3, help_text="Grade")
    social_stu_remark = models.CharField(max_length=10, help_text="Remark")

    creative_art_ca = models.CharField(max_length=2, help_text="C.A Score")
    creative_art_exam = models.CharField(max_length=2, help_text="Exam Score")
    creative_art_total = models.CharField(max_length=3, help_text="Total Course Score")
    creative_art_grade = models.CharField(max_length=3, help_text="Grade")
    creative_art_remark = models.CharField(max_length=10, help_text="Remark")

    phe_ca = models.CharField(max_length=2, help_text="C.A Score")
    phe_exam = models.CharField(max_length=2, help_text="Exam Score")
    phe_total = models.CharField(max_length=3, help_text="Total Course Score")
    phe_grade = models.CharField(max_length=3, help_text="Grade")
    phe_remark = models.CharField(max_length=10, help_text="Remark")

    home_economics_ca = models.CharField(max_length=2, help_text="C.A Score")
    home_economics_exam = models.CharField(max_length=2, help_text="Exam Score")
    home_economics_total = models.CharField(max_length=3, help_text="Total Course Score")
    home_economics_grade = models.CharField(max_length=3, help_text="Grade")
    home_economics_remark = models.CharField(max_length=10, help_text="Remark")

    bus_stu_ca = models.CharField(max_length=2, help_text="C.A Score")
    bus_stu_exam = models.CharField(max_length=2, help_text="Exam Score")
    bus_stu_total = models.CharField(max_length=3, help_text="Total Course Score")
    bus_stu_grade = models.CharField(max_length=3, help_text="Grade")
    bus_stu_remark = models.CharField(max_length=10, help_text="Remark")

    sec_edu_ca = models.CharField(max_length=2, help_text="C.A Score")
    sec_edu_exam = models.CharField(max_length=2, help_text="Exam Score")
    sec_edu_total = models.CharField(max_length=3, help_text="Total Course Score")
    sec_edu_grade = models.CharField(max_length=3, help_text="Grade")
    sec_edu_remark = models.CharField(max_length=10, help_text="Remark")
    
    agric_sci_ca = models.CharField(max_length=2, help_text="C.A Score")
    agric_sci_exam = models.CharField(max_length=2, help_text="Exam Score")
    agric_sci_total = models.CharField(max_length=3, help_text="Total Course Score")
    agric_sci_grade = models.CharField(max_length=3, help_text="Grade")
    agric_sci_remark = models.CharField(max_length=10, help_text="Remark")

    main_total = models.CharField(max_length=5, help_text="Total Term Score")
    no_in_class = models.CharField(max_length=5, help_text="Total of Students")
    class_name = models.CharField(max_length=5, help_text="Class name e.g. JIS1 ")
    term = models.CharField(max_length=15, help_text="Term of Session", choices=TERM_STATUS)
    session_year = models.CharField(max_length=10, help_text="Session")
    comment = models.CharField(max_length=30, help_text="Comment")
    objects = models.Manager()
    
    # Metadata
    class Meta: 
        ordering = ["student_name"]
    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.adm_no)+str(self.class_name)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.class_name+self.adm_no
 
class Jis(models.Model):
    """
    A Class defining JIS student result records.
    """
    # Fields
    student_name = models.CharField(max_length=20, help_text="Enter Student Name")
    adm_no = models.CharField(max_length=15, help_text="Enter Student Admission Number")
    average = models.CharField(max_length=15, help_text="Average Score in Term")
    position = models.CharField(max_length=5, help_text="Student's position in Term")
    
    quran_tafseer_ca = models.CharField(max_length=2, help_text="C.A Score")
    quran_tafseer_exam = models.CharField(max_length=2, help_text="Exam Score")
    quran_tafseer_total = models.CharField(max_length=3, help_text="Total Course Score")
    quran_tafseer_grade = models.CharField(max_length=3, help_text="Grade")
    quran_tafseer_remark = models.CharField(max_length=10, help_text="Remark")

    hadith_ca = models.CharField(max_length=2, help_text="C.A Score")
    hadith_exam = models.CharField(max_length=2, help_text="Exam Score")
    hadith_total = models.CharField(max_length=3, help_text="Total Course Score")
    hadith_grade = models.CharField(max_length=3, help_text="Grade")
    hadith_remark = models.CharField(max_length=10, help_text="Remark")

    tauheed_ca = models.CharField(max_length=2, help_text="C.A Score")
    tauheed_exam = models.CharField(max_length=2, help_text="Exam Score")
    tauheed_total = models.CharField(max_length=3, help_text="Total Course Score")
    tauheed_grade = models.CharField(max_length=3, help_text="Grade")
    tauheed_remark = models.CharField(max_length=10, help_text="Remark")

    fighu_ca = models.CharField(max_length=2, help_text="C.A Score")
    fighu_exam = models.CharField(max_length=2, help_text="Exam Score")
    fighu_total = models.CharField(max_length=3, help_text="Total Course Score")
    fighu_grade = models.CharField(max_length=3, help_text="Grade")
    fighu_remark = models.CharField(max_length=10, help_text="Remark")

    nahawu_ca = models.CharField(max_length=2, help_text="C.A Score")
    nahawu_exam = models.CharField(max_length=2, help_text="Exam Score")
    nahawu_total = models.CharField(max_length=3, help_text="Total Course Score")
    nahawu_grade = models.CharField(max_length=3, help_text="Grade")
    nahawu_remark = models.CharField(max_length=10, help_text="Remark")

    hausa_lan_ca = models.CharField(max_length=2, help_text="C.A Score")
    hausa_lan_exam = models.CharField(max_length=2, help_text="Exam Score")
    hausa_lan_total = models.CharField(max_length=3, help_text="Total Course Score")
    hausa_lan_grade = models.CharField(max_length=3, help_text="Grade")
    hausa_lan_remark = models.CharField(max_length=10, help_text="Remark")

    english_lan_ca = models.CharField(max_length=2, help_text="C.A Score")
    english_lan_exam = models.CharField(max_length=2, help_text="Exam Score")
    english_lan_total = models.CharField(max_length=3, help_text="Total Course Score")
    english_lan_grade = models.CharField(max_length=3, help_text="Grade")
    english_lan_remark = models.CharField(max_length=10, help_text="Remark")

    math_ca = models.CharField(max_length=2, help_text="C.A Score")
    math_exam = models.CharField(max_length=2, help_text="Exam Score")
    math_total = models.CharField(max_length=3, help_text="Total Course Score")
    math_grade = models.CharField(max_length=3, help_text="Grade")
    math_remark = models.CharField(max_length=10, help_text="Remark")

    basic_sci_ca = models.CharField(max_length=2, help_text="C.A Score")
    basic_sci_exam = models.CharField(max_length=2, help_text="Exam Score")
    basic_sci_total = models.CharField(max_length=3, help_text="Total Course Score")
    basic_sci_grade = models.CharField(max_length=3, help_text="Grade")
    basic_sci_remark = models.CharField(max_length=10, help_text="Remark")

    civic_edu_ca = models.CharField(max_length=2, help_text="C.A Score")
    civic_edu_exam = models.CharField(max_length=2, help_text="Exam Score")
    civic_edu_total = models.CharField(max_length=3, help_text="Total Course Score")
    civic_edu_grade = models.CharField(max_length=3, help_text="Grade")
    civic_edu_remark = models.CharField(max_length=10, help_text="Remark")

    adab_ca = models.CharField(max_length=2, help_text="C.A Score")
    adab_stu_exam = models.CharField(max_length=2, help_text="Exam Score")
    adab_stu_total = models.CharField(max_length=3, help_text="Total Course Score")
    adab_stu_grade = models.CharField(max_length=3, help_text="Grade")
    adab_stu_remark = models.CharField(max_length=10, help_text="Remark")

    creative_art_ca = models.CharField(max_length=2, help_text="C.A Score")
    creative_art_exam = models.CharField(max_length=2, help_text="Exam Score")
    creative_art_total = models.CharField(max_length=3, help_text="Total Course Score")
    creative_art_grade = models.CharField(max_length=3, help_text="Grade")
    creative_art_remark = models.CharField(max_length=10, help_text="Remark")

    phe_ca = models.CharField(max_length=2, help_text="C.A Score")
    phe_exam = models.CharField(max_length=2, help_text="Exam Score")
    phe_total = models.CharField(max_length=3, help_text="Total Course Score")
    phe_grade = models.CharField(max_length=3, help_text="Grade")
    phe_remark = models.CharField(max_length=10, help_text="Remark")

    home_economics_ca = models.CharField(max_length=2, help_text="C.A Score")
    home_economics_exam = models.CharField(max_length=2, help_text="Exam Score")
    home_economics_total = models.CharField(max_length=3, help_text="Total Course Score")
    home_economics_grade = models.CharField(max_length=3, help_text="Grade")
    home_economics_remark = models.CharField(max_length=10, help_text="Remark")

    bus_stu_ca = models.CharField(max_length=2, help_text="C.A Score")
    bus_stu_exam = models.CharField(max_length=2, help_text="Exam Score")
    bus_stu_total = models.CharField(max_length=3, help_text="Total Course Score")
    bus_stu_grade = models.CharField(max_length=3, help_text="Grade")
    bus_stu_remark = models.CharField(max_length=10, help_text="Remark")

    sec_edu_ca = models.CharField(max_length=2, help_text="C.A Score")
    sec_edu_exam = models.CharField(max_length=2, help_text="Exam Score")
    sec_edu_total = models.CharField(max_length=3, help_text="Total Course Score")
    sec_edu_grade = models.CharField(max_length=3, help_text="Grade")
    sec_edu_remark = models.CharField(max_length=10, help_text="Remark")
    
    agric_sci_ca = models.CharField(max_length=2, help_text="C.A Score")
    agric_sci_exam = models.CharField(max_length=2, help_text="Exam Score")
    agric_sci_total = models.CharField(max_length=3, help_text="Total Course Score")
    agric_sci_grade = models.CharField(max_length=3, help_text="Grade")
    agric_sci_remark = models.CharField(max_length=10, help_text="Remark")

    main_total = models.CharField(max_length=5, help_text="Total Term Score")
    no_in_class = models.CharField(max_length=5, help_text="Total of Students")
    class_name = models.CharField(max_length=5, help_text="Class name e.g. JIS1 ")
    term = models.CharField(max_length=15, help_text="Term of Session", choices=TERM_STATUS)
    session_year = models.CharField(max_length=10, help_text="Session")
    comment = models.CharField(max_length=30, help_text="Comment")
    objects = models.Manager()
    
    # Metadata
    class Meta: 
        ordering = ["student_name"]
    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.adm_no)+str(self.class_name)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.class_name+self.adm_no

        # Senior Secondary models
class Sas(models.Model):
    """
    A Class defining SAS student result records.
    """
    # Fields
    student_name = models.CharField(max_length=20, help_text="Enter Student Name")
    adm_no = models.CharField(max_length=15, help_text="Enter Student Admission Number")
    average = models.CharField(max_length=15, help_text="Average Score in Term")
    position = models.CharField(max_length=5, help_text="Student's position in Term")
    
    english_ca = models.CharField(max_length=2, help_text="C.A Score")
    english_exam = models.CharField(max_length=2, help_text="Exam Score")
    english_total = models.CharField(max_length=3, help_text="Total Course Score")
    english_grade = models.CharField(max_length=3, help_text="Grade")
    english_remark = models.CharField(max_length=10, help_text="Remark")

    hausa_ca = models.CharField(max_length=2, help_text="C.A Score")
    hausa_exam = models.CharField(max_length=2, help_text="Exam Score")
    hausa_total = models.CharField(max_length=3, help_text="Total Course Score")
    hausa_grade = models.CharField(max_length=3, help_text="Grade")
    hausa_remark = models.CharField(max_length=10, help_text="Remark")

    math_ca = models.CharField(max_length=2, help_text="C.A Score")
    math_exam = models.CharField(max_length=2, help_text="Exam Score")
    math_total = models.CharField(max_length=3, help_text="Total Course Score")
    math_grade = models.CharField(max_length=3, help_text="Grade")
    math_remark = models.CharField(max_length=10, help_text="Remark")

    islamic_ca = models.CharField(max_length=2, help_text="C.A Score")
    islamic_exam = models.CharField(max_length=2, help_text="Exam Score")
    islamic_total = models.CharField(max_length=3, help_text="Total Course Score")
    islamic_grade = models.CharField(max_length=3, help_text="Grade")
    islamic_remark = models.CharField(max_length=10, help_text="Remark")

    marketing_catering_ca = models.CharField(max_length=2, help_text="C.A Score")
    marketing_catering_exam = models.CharField(max_length=2, help_text="Exam Score")
    marketing_catering_total = models.CharField(max_length=3, help_text="Total Course Score")
    marketing_catering_grade = models.CharField(max_length=3, help_text="Grade")
    marketing_catering_remark = models.CharField(max_length=10, help_text="Remark")

    civil_edu_ca = models.CharField(max_length=2, help_text="C.A Score")
    civil_edu_exam = models.CharField(max_length=2, help_text="Exam Score")
    civil_edu_total = models.CharField(max_length=3, help_text="Total Course Score")
    civil_edu_grade = models.CharField(max_length=3, help_text="Grade")
    civil_edu_remark = models.CharField(max_length=10, help_text="Remark")

    account_biology_ca = models.CharField(max_length=2, help_text="C.A Score")
    account_biology_exam = models.CharField(max_length=2, help_text="Exam Score")
    account_biology_total = models.CharField(max_length=3, help_text="Total Course Score")
    account_biology_grade = models.CharField(max_length=3, help_text="Grade")
    account_biology_remark = models.CharField(max_length=10, help_text="Remark")

    commerce_chemistry_ca = models.CharField(max_length=2, help_text="C.A Score")
    commerce_chemistry_exam = models.CharField(max_length=2, help_text="Exam Score")
    commerce_chemistry_total = models.CharField(max_length=3, help_text="Total Course Score")
    commerce_chemistry_grade = models.CharField(max_length=3, help_text="Grade")
    commerce_chemistry_remark = models.CharField(max_length=10, help_text="Remark")

    economics_physics_ca = models.CharField(max_length=2, help_text="C.A Score")
    economics_physics_exam = models.CharField(max_length=2, help_text="Exam Score")
    economics_physics_total = models.CharField(max_length=3, help_text="Total Course Score")
    economics_physics_grade = models.CharField(max_length=3, help_text="Grade")
    economics_physics_remark = models.CharField(max_length=10, help_text="Remark")

    geography_ca = models.CharField(max_length=2, help_text="C.A Score")
    geography_exam = models.CharField(max_length=2, help_text="Exam Score")
    geography_total = models.CharField(max_length=3, help_text="Total Course Score")
    geography_grade = models.CharField(max_length=3, help_text="Grade")
    geography_remark = models.CharField(max_length=10, help_text="Remark")

    government_ca = models.CharField(max_length=2, help_text="C.A Score")
    government_exam = models.CharField(max_length=2, help_text="Exam Score")
    government_total = models.CharField(max_length=3, help_text="Total Course Score")
    government_grade = models.CharField(max_length=3, help_text="Grade")
    government_remark = models.CharField(max_length=10, help_text="Remark")

    creative_art_ca = models.CharField(max_length=2, help_text="C.A Score")
    creative_art_exam = models.CharField(max_length=2, help_text="Exam Score")
    creative_art_total = models.CharField(max_length=3, help_text="Total Course Score")
    creative_art_grade = models.CharField(max_length=3, help_text="Grade")
    creative_art_remark = models.CharField(max_length=10, help_text="Remark")

    phe_ca = models.CharField(max_length=2, help_text="C.A Score")
    phe_exam = models.CharField(max_length=2, help_text="Exam Score")
    phe_total = models.CharField(max_length=3, help_text="Total Course Score")
    phe_grade = models.CharField(max_length=3, help_text="Grade")
    phe_remark = models.CharField(max_length=10, help_text="Remark")

    home_economics_ca = models.CharField(max_length=2, help_text="C.A Score")
    home_economics_exam = models.CharField(max_length=2, help_text="Exam Score")
    home_economics_total = models.CharField(max_length=3, help_text="Total Course Score")
    home_economics_grade = models.CharField(max_length=3, help_text="Grade")
    home_economics_remark = models.CharField(max_length=10, help_text="Remark")

    bus_stu_ca = models.CharField(max_length=2, help_text="C.A Score")
    bus_stu_exam = models.CharField(max_length=2, help_text="Exam Score")
    bus_stu_total = models.CharField(max_length=3, help_text="Total Course Score")
    bus_stu_grade = models.CharField(max_length=3, help_text="Grade")
    bus_stu_remark = models.CharField(max_length=10, help_text="Remark")

    sec_edu_ca = models.CharField(max_length=2, help_text="C.A Score")
    sec_edu_exam = models.CharField(max_length=2, help_text="Exam Score")
    sec_edu_total = models.CharField(max_length=3, help_text="Total Course Score")
    sec_edu_grade = models.CharField(max_length=3, help_text="Grade")
    sec_edu_remark = models.CharField(max_length=10, help_text="Remark")
    
    agric_sci_ca = models.CharField(max_length=2, help_text="C.A Score")
    agric_sci_exam = models.CharField(max_length=2, help_text="Exam Score")
    agric_sci_total = models.CharField(max_length=3, help_text="Total Course Score")
    agric_sci_grade = models.CharField(max_length=3, help_text="Grade")
    agric_sci_remark = models.CharField(max_length=10, help_text="Remark")

    main_total = models.CharField(max_length=5, help_text="Total Term Score")
    no_in_class = models.CharField(max_length=5, help_text="Total of Students")
    class_name = models.CharField(max_length=5, help_text="Class name e.g. JIS1 ")
    term = models.CharField(max_length=15, help_text="Term of Session", choices=TERM_STATUS)
    session_year = models.CharField(max_length=10, help_text="Session")
    comment = models.CharField(max_length=30, help_text="Comment")
    objects = models.Manager()
    
    # Metadata
    class Meta: 
        ordering = ["student_name"]
    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.adm_no)+str(self.class_name)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.class_name+self.adm_no
 
class Sis(models.Model):
    """
    A Class defining SIS student result records.
    """
    # Fields
    student_name = models.CharField(max_length=20, help_text="Enter Student Name")
    adm_no = models.CharField(max_length=15, help_text="Enter Student Admission Number")
    average = models.CharField(max_length=15, help_text="Average Score in Term")
    position = models.CharField(max_length=5, help_text="Student's position in Term")
    
    quran_tafseer_ca = models.CharField(max_length=2, help_text="C.A Score")
    quran_tafseer_exam = models.CharField(max_length=2, help_text="Exam Score")
    quran_tafseer_total = models.CharField(max_length=3, help_text="Total Course Score")
    quran_tafseer_grade = models.CharField(max_length=3, help_text="Grade")
    quran_tafseer_remark = models.CharField(max_length=10, help_text="Remark")

    inshai_imlai_ca = models.CharField(max_length=2, help_text="C.A Score")
    inshai_imlai_exam = models.CharField(max_length=2, help_text="Exam Score")
    inshai_imlai_total = models.CharField(max_length=3, help_text="Total Course Score")
    inshai_imlai_grade = models.CharField(max_length=3, help_text="Grade")
    inshai_imlai_remark = models.CharField(max_length=10, help_text="Remark")

    hadis_musdalahu_ca = models.CharField(max_length=2, help_text="C.A Score")
    hadis_musdalahu_exam = models.CharField(max_length=2, help_text="Exam Score")
    hadis_musdalahu_total = models.CharField(max_length=3, help_text="Total Course Score")
    hadis_musdalahu_grade = models.CharField(max_length=3, help_text="Grade")
    hadis_musdalahu_remark = models.CharField(max_length=10, help_text="Remark")

    fighu_ca = models.CharField(max_length=2, help_text="C.A Score")
    fighu_exam = models.CharField(max_length=2, help_text="Exam Score")
    fighu_total = models.CharField(max_length=3, help_text="Total Course Score")
    fighu_grade = models.CharField(max_length=3, help_text="Grade")
    fighu_remark = models.CharField(max_length=10, help_text="Remark")

    tauhid_ca = models.CharField(max_length=2, help_text="C.A Score")
    tauhid_exam = models.CharField(max_length=2, help_text="Exam Score")
    tauhid_total = models.CharField(max_length=3, help_text="Total Course Score")
    tauhid_grade = models.CharField(max_length=3, help_text="Grade")
    tauhid_remark = models.CharField(max_length=10, help_text="Remark")

    mandik_ca = models.CharField(max_length=2, help_text="C.A Score")
    mandik_exam = models.CharField(max_length=2, help_text="Exam Score")
    mandik_total = models.CharField(max_length=3, help_text="Total Course Score")
    mandik_grade = models.CharField(max_length=3, help_text="Grade")
    mandik_remark = models.CharField(max_length=10, help_text="Remark")

    islamic_history_ca = models.CharField(max_length=2, help_text="C.A Score")
    islamic_history_exam = models.CharField(max_length=2, help_text="Exam Score")
    islamic_history_total = models.CharField(max_length=3, help_text="Total Course Score")
    islamic_history_grade = models.CharField(max_length=3, help_text="Grade")
    islamic_history_remark = models.CharField(max_length=10, help_text="Remark")

    nahawu_ca = models.CharField(max_length=2, help_text="C.A Score")
    nahawu_exam = models.CharField(max_length=2, help_text="Exam Score")
    nahawu_total = models.CharField(max_length=3, help_text="Total Course Score")
    nahawu_grade = models.CharField(max_length=3, help_text="Grade")
    nahawu_remark = models.CharField(max_length=10, help_text="Remark")

    balaga_ca = models.CharField(max_length=2, help_text="C.A Score")
    balaga_exam = models.CharField(max_length=2, help_text="Exam Score")
    balaga_total = models.CharField(max_length=3, help_text="Total Course Score")
    balaga_grade = models.CharField(max_length=3, help_text="Grade")
    balaga_remark = models.CharField(max_length=10, help_text="Remark")

    adab_ca = models.CharField(max_length=2, help_text="C.A Score")
    adab_exam = models.CharField(max_length=2, help_text="Exam Score")
    adab_total = models.CharField(max_length=3, help_text="Total Course Score")
    adab_grade = models.CharField(max_length=3, help_text="Grade")
    adab_remark = models.CharField(max_length=10, help_text="Remark")

    arud_ca = models.CharField(max_length=2, help_text="C.A Score")
    arud_exam = models.CharField(max_length=2, help_text="Exam Score")
    arud_total = models.CharField(max_length=3, help_text="Total Course Score")
    arud_grade = models.CharField(max_length=3, help_text="Grade")
    arud_remark = models.CharField(max_length=10, help_text="Remark")

    tarjama_ca = models.CharField(max_length=2, help_text="C.A Score")
    tarjama_exam = models.CharField(max_length=2, help_text="Exam Score")
    tarjama_total = models.CharField(max_length=3, help_text="Total Course Score")
    tarjama_grade = models.CharField(max_length=3, help_text="Grade")
    tarjama_remark = models.CharField(max_length=10, help_text="Remark")

    computer_ca = models.CharField(max_length=2, help_text="C.A Score")
    computer_exam = models.CharField(max_length=2, help_text="Exam Score")
    computer_total = models.CharField(max_length=3, help_text="Total Course Score")
    computer_grade = models.CharField(max_length=3, help_text="Grade")
    computer_remark = models.CharField(max_length=10, help_text="Remark")

    english_language_ca = models.CharField(max_length=2, help_text="C.A Score")
    english_language_exam = models.CharField(max_length=2, help_text="Exam Score")
    english_language_total = models.CharField(max_length=3, help_text="Total Course Score")
    english_language_grade = models.CharField(max_length=3, help_text="Grade")
    english_language_remark = models.CharField(max_length=10, help_text="Remark")

    hausa_language_ca = models.CharField(max_length=2, help_text="C.A Score")
    hausa_language_exam = models.CharField(max_length=2, help_text="Exam Score")
    hausa_language_total = models.CharField(max_length=3, help_text="Total Course Score")
    hausa_language_grade = models.CharField(max_length=3, help_text="Grade")
    hausa_language_remark = models.CharField(max_length=10, help_text="Remark")

    maths_ca = models.CharField(max_length=2, help_text="C.A Score")
    maths_exam = models.CharField(max_length=2, help_text="Exam Score")
    maths_total = models.CharField(max_length=3, help_text="Total Course Score")
    maths_grade = models.CharField(max_length=3, help_text="Grade")
    maths_remark = models.CharField(max_length=10, help_text="Remark")

    home_economics_ca = models.CharField(max_length=2, help_text="C.A Score")
    home_economics_exam = models.CharField(max_length=2, help_text="Exam Score")
    home_economics_total = models.CharField(max_length=3, help_text="Total Course Score")
    home_economics_grade = models.CharField(max_length=3, help_text="Grade")
    home_economics_remark = models.CharField(max_length=10, help_text="Remark")
    
    agric_sci_ca = models.CharField(max_length=2, help_text="C.A Score")
    agric_sci_exam = models.CharField(max_length=2, help_text="Exam Score")
    agric_sci_total = models.CharField(max_length=3, help_text="Total Course Score")
    agric_sci_grade = models.CharField(max_length=3, help_text="Grade")
    agric_sci_remark = models.CharField(max_length=10, help_text="Remark")

    civic_edu_ca = models.CharField(max_length=2, help_text="C.A Score")
    civic_edu_exam = models.CharField(max_length=2, help_text="Exam Score")
    civic_edu_total = models.CharField(max_length=3, help_text="Total Course Score")
    civic_edu_grade = models.CharField(max_length=3, help_text="Grade")
    civic_edu_remark = models.CharField(max_length=10, help_text="Remark")


    mudalia_ca = models.CharField(max_length=2, help_text="C.A Score")
    mudalia_exam = models.CharField(max_length=2, help_text="Exam Score")
    mudalia_total = models.CharField(max_length=3, help_text="Total Course Score")
    mudalia_grade = models.CharField(max_length=3, help_text="Grade")
    mudalia_remark = models.CharField(max_length=10, help_text="Remark")


    main_total = models.CharField(max_length=5, help_text="Total Term Score")
    no_in_class = models.CharField(max_length=5, help_text="Total of Students")
    class_name = models.CharField(max_length=5, help_text="Class name e.g. JIS1 ")
    term = models.CharField(max_length=15, help_text="Term of Session", choices=TERM_STATUS)
    session_year = models.CharField(max_length=10, help_text="Session")
    comment = models.CharField(max_length=30, help_text="Comment")
    objects = models.Manager()
    
    # Metadata
    class Meta: 
        ordering = ["student_name"]
    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.adm_no)+str(self.class_name)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.class_name+self.adm_no 

class Studentsdata(models.Model):
    """
    A Class defining student bio data.
    """
    CLASSES = (
        ('Jas 1', 'Jas 1'),
        ('Jas 2', 'Jas 2'),
        ('Jas 3', 'Jas 3'),
        ('Jis 1', 'Jis 1'),
        ('Jis 2', 'Jis 2'),
        ('Jis 3', 'Jis 3'),
        ('Sas 1', 'Sas 1'),
        ('Sas 2', 'Sas 2'),
        ('Sas 3', 'Sas 3'),
        ('Sis 1', 'Sis 1'),
        ('Sis 2', 'Sis 2'),
        ('Sis 3', 'Sis 3'),
    )

    YEAR = (
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
        ('2033', '2033'),
        ('2034', '2034'),
        ('2035', '2035'),
        ('2036', '2036'),
        ('2037', '2037'),
        ('2038', '2038'),
        ('2039', '2039'),
        ('2040', '2040'),
        ('2041', '2041'),
        ('2042', '2042'),
        ('2043', '2043'),
    )
    student_name = models.CharField(max_length=20, help_text="Enter Student Name")
    adm_no = models.CharField(max_length=15, help_text="Enter Student Admission Number",)
    date_of_birth = models.DateField(help_text='Date of Birth')
    primary_school = models.CharField(max_length=50, help_text="Primary School Attended")
    parent = models.CharField(max_length=20, help_text='Parent/Guardian Name')
    date_registered = models.DateField(default=timezone.now )
    address = models.CharField(max_length=50, help_text='Address')
    telephone = models.CharField(max_length=15, help_text="Phone/Telephone")
    section = models.CharField(max_length=30, help_text='Section')
    class_name = models.CharField(max_length=5, help_text='Class Name',choices=CLASSES)
    admission_year = models.CharField(max_length=5, help_text='Class Name',choices=YEAR)
    image = models.CharField(max_length=250, help_text='Image')
    
    objects = models.Manager()
    
    # Metadata
    class Meta: 
        ordering = ["-date_registered", "student_name" ]
    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         sp = " "
         return reverse('model-detail-view', args=[str(self.adm_no) + sp + str(self.class_name)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        sp = " "
        return self.class_name+sp+self.adm_no +sp+self.student_name
