from django import forms

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
class UploadResultForm(forms.Form):
    class_name = forms.ChoiceField(choices=CLASSES )
    file = forms.FileField()