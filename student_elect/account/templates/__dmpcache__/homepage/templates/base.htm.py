# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551563710.037388
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/student_elect/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(' - StudentElect</title>\n    <meta name="description" content="">\n    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no, shrink-to-fit=no, viewport-fit=cover">\n    <meta name="robots" content="all,follow">\n    <meta name="apple-mobile-web-app-capable" content="yes">\n    <meta name="apple-mobile-web-app-status-bar-style" content="default">\n    \n    <!-- Font Awesome -->\n    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css">\n    <!-- Bootstrap core CSS -->\n    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.2.1/css/bootstrap.min.css" rel="stylesheet">\n    <!-- Material Design Bootstrap -->\n    <link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.7.0/css/mdb.min.css" rel="stylesheet">\n    <!-- Fontastic Custom icon font-->\n    <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/css/fontastic.css">\n    <!-- Google fonts - Poppins -->\n    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">\n    <!-- theme stylesheet-->\n    <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/css/style.default.css" id="theme-stylesheet">\n\n    <!-- Favicon-->\n    <link rel="shortcut icon" href="img/favicon.ico">\n\n    <!-- JQuery -->\n    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n    <!-- Bootstrap tooltips -->\n    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>\n    <!-- Bootstrap core JavaScript -->\n    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.2.1/js/bootstrap.min.js"></script>\n    <!-- MDB core JavaScript -->\n    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.7.0/js/mdb.min.js"></script>\n    \n\n    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n\n  </head>\n  <body>\n    <div class="page">\n\n      <!-- Main Navbar-->\n      <header class="header">\n          <nav class="fixed-top" id="navigation">\n\n            <div class="container-fluid">\n              <div class="row justify-content-center">\n\n                <nav class="navbar navbar-expand-lg navbar-light col-lg-9">\n                  <button class="navbar-toggler collapsed" id="hamburger-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\n                    <span class="navbar-toggler-icon"></span>\n                  </button>\n          \n                  <a class="navbar-brand" href="#"><img id="site-logo" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/python.png"></a>\n          \n                  <button class="navbar-settings">\n                    <span class="navbar-toggler-icon" id="settings-icon"></span>\n                  </button>\n                \n                  <div class="collapse navbar-collapse" id="navbarSupportedContent">\n                    <ul class="navbar-nav mr-auto">\n                      <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'polls' else ''))
        __M_writer('">\n                        <a class="nav-link" href="#" id="polls"><strong>Polls</strong></a>\n                      </li>\n                      <li class="nav-item">\n                        <a class="nav-link" href="#" id="submissions"><strong>Submissions</strong></a>\n                      </li>\n                    </ul>\n                    <ul class="navbar-nav">\n')
        if request.user.is_authenticated:
            __M_writer('                        <li class="nav-item">\n                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                                Account\n                            </a>\n                            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">\n                                <a class="dropdown-item" href="#">Settings</a>\n                                <div class="dropdown-divider"></div>\n                                <a class="dropdown-item" href="/account/logout">Sign out</a>\n                            </div>\n                        </li>\n')
        else:
            __M_writer('                        <li class="nav-item">\n                            <a class="nav-link-right nav-link text-dark" href="/account/login">Sign in</a>\n                        </li>\n                        <li class="nav-item">\n                            <a class="nav-link-right nav-link text-dark" href="/account/register">Register</a>\n                        </li>\n')
        __M_writer('\n                    </ul>\n                  </div>\n                </nav>\n\n              </div>\n            </div>\n          </nav>\n      </header>\n\n      <div class="page-content d-flex align-items-stretch"> \n        <div class="content-inner">\n\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('             \n\n        </div>\n      </div>\n\n    </div>\n\n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/student_elect/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "30": 1, "35": 7, "36": 21, "37": 21, "38": 25, "39": 25, "40": 40, "41": 40, "42": 59, "43": 59, "44": 67, "45": 67, "46": 76, "47": 77, "48": 87, "49": 88, "50": 95, "55": 108, "61": 7, "72": 108, "83": 72}}
__M_END_METADATA
"""
