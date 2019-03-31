from django_mako_plus import dmp_path

urlpatterns = [
    # Because these patterns are subpatterns within the app's resolver,
    # we don't include the /app/ in the pattern -- it's already been
    # handled by the app's resolver.
    #
    # Also note how the each pattern below defines the four kwargs--
    # either as 1) a regex named group or 2) in kwargs.
    
    dmp_path(
        r'^',
        { 'dmp_app': 'dashboard',
        'dmp_page': 'active',
        'dmp_function': 'process_request',
        'dmp_urlparams': '' },
        name='/dashboard/',
    ),
]