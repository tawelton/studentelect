from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django_mako_plus import view_function, jscontext
from poll import models as mods
from datetime import datetime, timezone

@login_required
@view_function
def process_request(request):

    return request.dmp.render('active.html', { 
        'polls': mods.Poll.objects.filter(Q(status='A') | Q(status='I')).filter(user=request.user),
     })