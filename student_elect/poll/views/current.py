from django.contrib.auth.decorators import login_required
from django.conf import settings
from django_mako_plus import view_function, jscontext
from account import models as amods
from poll import models as mods
from poll import forms
from datetime import datetime, timezone
from django.http import HttpResponseRedirect, HttpResponse, Http404
import json

@view_function
def process_request(request, username:str=''):

    user = amods.User.objects.filter(username=username).first()
    if user is None:
        raise Http404

    polls = user.poll_set.filter(status='A')

    return request.dmp.render('current.html', {
        'polls': polls,
        'user': user,
        jscontext('username'): username,
    })

@view_function
def getlogin(request, username:str='', pollID:int=None):

    user = amods.User.objects.filter(username=username).first()
    if user is None:
        raise Http404

    poll = user.poll_set.filter(status='A', id=pollID).first()

    #  if poll doesn't exist, go back to polls page
    if poll is None:
        return HttpResponseRedirect('/poll/' + username + '/current/')

    # if poll has no student id records, skip login and go to candidates page 
    if poll.student_set.all().count() == 0:
        return HttpResponseRedirect('/poll/' + username + '/current.getactivecandidates/' + str(pollID))

    # otherwise, return the login page
    return request.dmp.render('current.getlogin.html', {
        'poll': poll,
        'user': user,
    })

@view_function
def login(request, username:str='', pollID:int=None):

    user = amods.User.objects.filter(username=username).first()
    if user is None:
        raise Http404

    poll = user.poll_set.filter(id=pollID).first()

    #  if poll doesn't exist, go back to polls page
    if poll is None:
        return HttpResponseRedirect('/poll/' + username + '/current/')


    # if student ID is valid, redirect request to candidate page

    if poll.student_set.filter(studentID=request.POST.get('studentID')).count() > 0:
        return HttpResponseRedirect('/poll/' + username + '/current.getactivecandidates/' + str(pollID) + '/' + request.POST.get('studentID'))
    # if invalid, return a 403 forbidden code
    else:
        return HttpResponse(status=403)

@view_function
def getactivecandidates(request, username:str='', pollID:int=None, studentID:int=None):

    user = amods.User.objects.filter(username=username).first()
    if user is None:
        raise Http404

    poll = user.poll_set.filter(id=pollID).first()

    #  if poll doesn't exist, go back to polls page
    if poll is None:
        return HttpResponseRedirect('/poll/' + username + '/current/')

    print(studentID)

    # if student ID is invalid and the poll does not have any student ID records, redirect request to candidate page

    if poll.student_set.filter(studentID=str(studentID)).count() == 0 and poll.student_set.all().count() != 0:
        return HttpResponse(status=403)
    # if invalid, return a 403 forbidden code
    
    candidates = mods.Candidate.objects.filter(poll_id=pollID, status='A').order_by('?')


    return request.dmp.render('current.getactivecandidates.html', 
    { 
        'candidates': candidates,
        'poll': poll,
        jscontext('votelimit'): poll.votelimit,
        jscontext('username'): username,
        jscontext('pollID'): pollID,
        jscontext('studentID'): studentID,
    })

@view_function
def submitvotes(request, username:str='', pollID:int=None, studentID:int=None):

    user = amods.User.objects.filter(username=username).first()
    if user is None:
        raise Http404

    poll = user.poll_set.filter(id=pollID).first()

    #  if poll doesn't exist, go back to polls page
    if poll is None:
        return HttpResponseRedirect('/poll/' + username + '/current/')


    # if student ID is invalid and the poll does have student ID records, return 403 error

    student = poll.student_set.filter(studentID=studentID).first()

    if student is None and poll.student_set.all().count() != 0:
        return HttpResponse(status=403)

    if request.is_ajax():
        if request.method == 'POST':
            candidateIDs = json.loads(request.body).get('candidates')

            # return 'bad request' if candidates array is unavailable
            if candidateIDs is None:
                return HttpResponse(status=400)

            # return 'not acceptable' if more votes than vote limit
            if len(candidateIDs) > poll.votelimit:
                return HttpResponse(status=406)

            # delete all previous votes
            poll.vote_set.filter(student=student).delete()

            votes = []

            for candidateID in candidateIDs:
                vote = mods.Vote()

                vote.round = poll.round
                vote.student = poll.student_set.filter(studentID=studentID).first()
                vote.poll = poll

                vote.candidate = poll.candidate_set.filter(id=candidateID).first()
                
                # if candidate is valid for the poll, add to array
                if vote.candidate is not None:
                    votes.append(vote)

            mods.Vote.objects.bulk_create(votes)

    return request.dmp.render('current.success.html')

    