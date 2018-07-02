from django.shortcuts import render, redirect
from .models import Jas, Jis, Sas, Sis, Studentsdata
from django.utils import timezone 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv, os
# Create your views here.
 
def check_report(request):
    if request.method == 'POST':
        adm_no = request.POST.get('adm_no')
        year = request.POST.get('session_year')
        class_name = request.POST.get('class_name')
        term = request.POST.get('term')
        print(adm_no,year, class_name, term)
        if class_name.lower().startswith("jas"):
            student = Jas.objects.filter(adm_no=adm_no, class_name=class_name, session_year__startswith=year, term=term)
            return render (request, 'reportsheet_jas.html', {'student' : student, 'date': timezone.localdate} )
        elif class_name.lower().startswith("jis"):
            student = Jis.objects.filter(adm_no=adm_no, class_name=class_name, session_year__startswith=year, term=term)
            return render (request, 'reportsheet_jis.html', {'student' : student, 'date': timezone.localdate} )
        elif class_name.lower().startswith("sas"):
            student = Sas.objects.filter(adm_no=adm_no, class_name=class_name, session_year__startswith=year, term=term)
            return render (request, 'reportsheet_sas.html', {'student' : student, 'date': timezone.localdate} )
        elif class_name.lower().startswith("sis"):
            student = Sis.objects.filter(adm_no=adm_no, class_name=class_name, session_year__startswith=year, term=term)
            return render (request, 'reportsheet_sis.html', {'student' : student, 'date': timezone.localdate} )
        else: 
           return render (request, 'resulterror.html')
    else:
        return render(request, 'students.html')
        
def students(request):
    return render(request, 'students.html')

def student_profile(request):
    if request.method == 'POST':
        adm_no = request.POST.get('adm_no')
        class_name = request.POST.get('class_name')
        print(adm_no,class_name, )
        student = Studentsdata.objects.filter(adm_no=adm_no,  class_name=class_name,)
        return render (request, 'student_profile.html', {student:'student'})
    else:
        return render (request, 'students.html')

def student_result(request):
    return render (request, 'studentsresult.html')

def staffs(request):
    return render (request, 'staffs.html')

def student_bio_data(request):
    return render (request, 'studentsdata.html')

def uploaddata(request):
    fs = FileSystemStorage('/tmp')
    if request.method == 'POST':
        #file_name = request.FILES['myfile'] 
        #class_name = request.POST.get('class_name')
        #print(file_name, class_name)
        myfile = request.FILES['myfile']
        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        with fs.open(uploaded_file_url, 'r') as fileupload:
            dta = csv.reader(fileupload)
            for row in dta:
                if len(row[0]) >3 and row[0] != 'STD NAME':
                    print(row)

        return render(request, 'upload_finish.html')