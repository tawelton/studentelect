from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.contrib.auth import authenticate, login
from django import forms
from django.http import HttpResponseRedirect

from pprint import pprint

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Username', 
        widget=forms.TextInput(
            attrs={"class":"form-control"}
            ),
        max_length = 50
        )

    password = forms.CharField(
        label = 'Password', 
        widget=forms.PasswordInput(
            attrs={"class":"form-control"}
            )
        )

    remember_me = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput()
        )

    def clean(self):

        # Login user
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        
        if user is None:
            raise forms.ValidationError('Invalid username or password.')
        
        return self.cleaned_data

@view_function
def process_request(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():

            print("FORM: ",form.cleaned_data.get("username"))
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

            login(request, user)
            return HttpResponseRedirect('/')
        else:
            

    else:
        form = LoginForm()
        
    context = {
            'form': form,
        }

    pprint(form.username)

    return request.dmp.render('login.html', context)