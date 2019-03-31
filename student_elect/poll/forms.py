from poll import models
from django import forms
from django.core.validators import FileExtensionValidator

class PollForm(forms.ModelForm):
    class Meta:
        model = models.Poll
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
    
class CandidateForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['firstname', 'lastname', 'imagefile']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'imagefile': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'imagefile': 'Image File',
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['studentID']
        widgets = {
            'studentID': forms.TextInput()
        }

class SettingsForm(forms.Form):
    votelimit = forms.IntegerField(
        label="Votes allowed per user", 
        required=False, 
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
            ),
        )
    students = forms.FileField(
        label="Student IDs",
        required = False,
        help_text="Upload a .csv file containing the student IDs of those permitted to vote in this poll. <p class=\"text-danger\">Make sure the first row in the student ID column is labeld \"ID\"</p>",  
        validators=[FileExtensionValidator(allowed_extensions=['csv'])],
        widget=forms.FileInput(
            attrs={'class': 'form-control-file'}
            ),
        )
