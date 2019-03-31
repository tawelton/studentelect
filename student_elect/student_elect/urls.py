"""student_elect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django_mako_plus import dmp_path

urlpatterns = [
    # the built-in Django administrator
    url(r'^admin/', admin.site.urls),

    # urls for any third-party apps go here

    # include the poll app urls.py file
    url('^poll/?', include('poll.urls')),

    # the DMP router - this should normally be the last URL listed
    url('', include('django_mako_plus.urls')),

    dmp_path(
        '^dashboard',
        { 'dmp_app': 'dashboard',
        'dmp_page': 'active',
        'dmp_function': 'process_request',
        'dmp_urlparams': '' },
        name='/dashboard/',
    ),

    url(r'^(?P<username>[_a-zA-Z0-9\-]+)/?', include('poll.urls'))
]
