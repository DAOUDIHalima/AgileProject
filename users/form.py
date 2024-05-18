from django import forms
from .models import Prof ,Student
from django.forms import DateInput, SelectDateWidget, ModelForm

from django import forms


#########PatientForm
class ProfForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = fields = ['First_name', 'Last_name', 'addressMail', 'Matricule']
        widgets = {
            'area': forms.Select(attrs={'class': 'form-select mr-sm-2'}),
         }

#########PatientForm
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = fields = ['First_name', 'Last_name', 'addressMail', 'Matricule']
        widgets = {
            'area': forms.Select(attrs={'class': 'form-select mr-sm-2'}),
         } 