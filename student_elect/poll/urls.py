from django_mako_plus import dmp_path

urlpatterns = [
    # Because these patterns are subpatterns within the app's resolver,
    # we don't include the /app/ in the pattern -- it's already been
    # handled by the app's resolver.
    #
    # Also note how the each pattern below defines the four kwargs--
    # either as 1) a regex named group or 2) in kwargs.
    dmp_path(
        r'^(?P<username>[_a-zA-Z0-9\-]+)/(?P<dmp_page>[_a-zA-Z0-9\-]+)\.(?P<dmp_function>[_a-zA-Z0-9\.\-]+)/(?P<dmp_urlparams>.+?)/?$',
        { 'dmp_app': 'poll' },
        name='/poll/username/page.function/urlparams',
    ),
    dmp_path(
        r'^(?P<username>[_a-zA-Z0-9\-]+)/(?P<dmp_page>[_a-zA-Z0-9\-]+)\.(?P<dmp_function>[_a-zA-Z0-9\.\-]+)/?$',
        { 'dmp_app': 'poll',
        'dmp_urlparams': '' },
        name='/poll/username/page.function',
    ),
    dmp_path(
        r'^(?P<username>[_a-zA-Z0-9\-]+)/(?P<dmp_page>[_a-zA-Z0-9\-]+)/(?P<dmp_urlparams>.+?)/?$',
        { 'dmp_app': 'poll',
        'dmp_function': 'process_request' },
        '/poll/username/page/urlparams',
    ),
    dmp_path(
        r'^(?P<username>[_a-zA-Z0-9\-]+)/(?P<dmp_page>[_a-zA-Z0-9\-]+)/?$',
        { 'dmp_app': 'poll',
            'dmp_function': 'process_request',
            'dmp_urlparams': '' },
        name='/poll/username/page',
    ),
    dmp_path(
        r'^(?P<username>[_a-zA-Z0-9\-]+)/?$',
        { 'dmp_app': 'poll',
        'dmp_page': 'current',
        'dmp_function': 'process_request',
        'dmp_urlparams': '' },
        name='/poll/username',
    ),
    dmp_path(
        r'^',
        { 'dmp_app': 'poll',
        'dmp_page': 'current',
        'dmp_function': 'process_request',
        'dmp_urlparams': '' },
        name='/username',
    ),
]