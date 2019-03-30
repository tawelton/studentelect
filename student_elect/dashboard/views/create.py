from django.contrib.auth.decorators import login_required
from django.conf import settings
from django_mako_plus import view_function, jscontext
from account.models import User
from poll import models as mods
from poll import forms
from datetime import datetime, timezone
from django.http import HttpResponseRedirect

@login_required
@view_function
def process_request(request, poll: int = None):

    pollform = forms.PollForm()

    if request.method == 'POST':
        pollform = forms.PollForm(request.POST)

        if pollform.is_valid():
            print(">>>>>>>>")

            poll = pollform.save(commit=False)

            print(poll)

            poll.user = request.user
            poll.save()

            return HttpResponseRedirect("/dashboard/edit/" + str(poll.id))

    return request.dmp.render('create.html', { 
        'pollform': pollform,
    })