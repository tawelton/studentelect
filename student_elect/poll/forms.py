from poll import models
from django import forms

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
