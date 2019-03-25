from django.contrib.auth.decorators import login_required
from django.conf import settings
from django_mako_plus import view_function, jscontext
from account.models import User
from poll import models as mods
from poll import forms
from datetime import datetime, timezone

@login_required
@view_function
def process_request(request):

    candidateform = forms.CandidateForm()

    print(">>>>>>>before")

    print(request.method)

    if request.method == 'POST':

        candidateform = forms.CandidateForm(request.POST, request.FILES)
        candidate = candidateform.save(commit=False)

        candidate.poll = mods.Poll.objects.get(id=1)

        candidate.status = 'A'
        candidate.round = 1

        print(">>>>>>>>>>>>")
        print(candidate.poll)

        candidate.save()

    return request.dmp.render('candidate.html', { 
        'candidateform': candidateform,
    })