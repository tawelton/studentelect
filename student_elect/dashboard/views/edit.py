from django.contrib.auth.decorators import login_required
from django.conf import settings
from django_mako_plus import view_function, jscontext
from account.models import User
from poll import models as mods
from poll import forms
from datetime import datetime, timezone
from django.http import HttpResponseRedirect, HttpResponse
from pprint import pprint

@login_required
@view_function
def process_request(request, poll: int = None):

    return request.dmp.render('edit.html', 
    { 
        'candidateform': forms.CandidateForm(),
        jscontext('pollID'): poll,
        'poll': mods.Poll.objects.filter(id=poll).first()
    })

@login_required
@view_function
def addcandidate(request, poll: int = None):

    candidateform = forms.CandidateForm()

    if request.method == 'POST':

        candidateform = forms.CandidateForm(request.POST, request.FILES)

        candidate = candidateform.save(commit=False)

        candidate.poll = mods.Poll.objects.get(id=poll)
        candidate.status = 'A'

        candidate.save()

    return HttpResponse('')

@login_required
@view_function
def deletecandidate(request, candidateID: int = None):

    if request.method == 'POST':

        candidate = mods.Candidate.objects.filter(id=candidateID).first()
        candidate.status = "I"
        candidate.save()

    return HttpResponse('')

@login_required
@view_function
def getactivecandidates(request, poll: int = None):

    candidates = mods.Candidate.objects.filter(poll_id=poll, status='A')

    return request.dmp.render('edit.getactivecandidates.html', 
    { 
        'candidates': candidates,
        'poll': mods.Poll.objects.filter(id=poll).first(),
    })

@login_required
@view_function
def getinactivecandidates(request, poll: int = None):

    candidates = mods.Candidate.objects.filter(poll_id=poll, status='I')

    return request.dmp.render('edit.getinactivecandidates.html', 
    { 
        'candidates': candidates,
    })

@login_required
@view_function
def togglepollstatus(request, pollID: int = None):

    if request.method == 'POST':

        poll = mods.Poll.objects.filter(id=pollID).first()

        if poll.status == "A":
            poll.status = "I"
        else:
            poll.status = "A"

        poll.save()

    return HttpResponse('')

@login_required
@view_function
def endpoll(request, pollID: int = None):

    if request.method == 'POST':

        poll = mods.Poll.objects.filter(id=pollID).first()

        poll.status = "C"

        poll.save()

    return HttpResponse('')


@login_required
@view_function
def deletepoll(request, pollID: int = None):

    if request.method == 'POST':

        poll = mods.Poll.objects.filter(id=pollID).first()

        poll.status = "D"

        poll.save()

    return HttpResponse('')