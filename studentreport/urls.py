from django.conf.urls import url
from .views import students, check_report, student_result, student_bio_data, staffs, uploaddata, student_profile

 
urlpatterns = [
    url(r'^$', students, name='students'),
    url(r'^check_report/', check_report, name='check_report'), 
    url(r'^student_result/', student_result, name='student_result'),
    url(r'^student_bio_data/', student_bio_data, name='student_bio_data'),
    url(r'^staffs/', staffs, name='staffs'),
    url(r'^uploaddata/', uploaddata, name='uploaddata'), 
    url(r'^student_profile/', student_profile, name='student_profile'), 
]

