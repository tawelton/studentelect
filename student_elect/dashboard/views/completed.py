from django.contrib.auth.decorators import login_required
from django.conf import settings
from django_mako_plus import view_function, jscontext
from poll import models as mods
from datetime import datetime, timezone

@login_required
@view_function
def process_request(request):

    return request.dmp.render('completed.html', { 
        'polls': mods.Poll.objects.filter(user=request.user, status='C'),
     })