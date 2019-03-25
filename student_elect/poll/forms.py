from poll import models
from django import forms

class PollForm(forms.ModelForm):
    class Meta:
        model = models.Poll
        fields = ['title']
        widgets = {
            'title': forms.TextInput()
        }
    
class CandidateForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['firstname', 'lastname', 'imagefile']
        widgets = {
            'firstname': forms.TextInput(),
            'lastname': forms.TextInput(),
            'imagefile': forms.FileInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['studentID']
        widgets = {
            'studentID': forms.TextInput()
        }
