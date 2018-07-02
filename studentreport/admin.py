from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Jis, Jas, Sas, Sis, Studentsdata

class JasResource(resources.ModelResource):
    class Meta:
        model = Jas
class JasResult(ImportExportModelAdmin):
    resource_class = JasResource
    list_filter = ('term', 'session_year',)

class JisResource(resources.ModelResource):
    class Meta:
        model = Jas
class JisResult(ImportExportModelAdmin):
    resource_class = JisResource
    list_filter = ('term', 'session_year',)

class SasResource(resources.ModelResource):
    class Meta:
        model = Sas
class SasResult(ImportExportModelAdmin):
    resource_class = SasResource
    list_filter = ('term', 'session_year',)

class SisResource(resources.ModelResource):
    class Meta:
        model = Sis
class SisResult(ImportExportModelAdmin):
    resource_class = SisResource
    list_filter = ('term', 'session_year',)

class StudentResource(resources.ModelResource):
    class Meta:
        model = Studentsdata
class StudentsInfo(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ('student_name','admission_year','adm_no','section','class_name', 'date_of_birth', 'parent','telephone')
    list_filter = ('date_registered', 'class_name', 'section', 'admission_year')

# models register here.
admin.site.register(Jis, JisResult)
admin.site.register(Jas, JasResult) 
admin.site.register(Sis, SisResult)
admin.site.register(Sas, SasResult)
admin.site.register(Studentsdata, StudentsInfo)