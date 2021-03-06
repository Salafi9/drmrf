# Generated by Django 2.0.6 on 2018-06-29 20:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentreport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentsdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(help_text='Enter Student Name', max_length=20)),
                ('adm_no', models.CharField(help_text='Enter Student Admission Number', max_length=15)),
                ('date_of_birth', models.DateField(help_text='Date of Birth')),
                ('primary_school', models.CharField(help_text='Primary School Attended', max_length=50)),
                ('parent', models.CharField(help_text='Parent/Guardian Name', max_length=20)),
                ('date_registered', models.DateField(default=django.utils.timezone.localdate)),
                ('address', models.CharField(help_text='Address', max_length=50)),
                ('telephone', models.CharField(help_text='Phone/Telephone', max_length=15)),
                ('section', models.CharField(help_text='Section', max_length=30)),
                ('class_name', models.CharField(choices=[('Jas 1', 'Jas 1'), ('Jas 2', 'Jas 2'), ('Jas 3', 'Jas 3'), ('Jis 1', 'Jis 1'), ('Jis 2', 'Jis 2'), ('Jis 3', 'Jis 3'), ('Sas 1', 'Sas 1'), ('Sas 2', 'Sas 2'), ('Sas 3', 'Sas 3'), ('Sis 1', 'Sis 1'), ('Sis 2', 'Sis 2'), ('Sis 3', 'Sis 3')], help_text='Class Name', max_length=5)),
            ],
            options={
                'ordering': ['-date_registered', 'student_name'],
            },
        ),
    ]
