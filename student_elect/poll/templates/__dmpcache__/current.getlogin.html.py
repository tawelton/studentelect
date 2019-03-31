# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554064522.643328
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/poll/templates/current.getlogin.html'
_template_uri = 'current.getlogin.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        poll = context.get('poll', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
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
        self = context.get('self', UNDEFINED)
        poll = context.get('poll', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="container">\n        <div class="row justify-content-center">\n            <div class="col-lg-5 col-md-7 col-sm-8 m-3">\n              <form method="POST" action="/poll/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( user.username ))
        __M_writer('/current.login/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( poll.id ))
        __M_writer('" id="studentForm">\n                <div class="card">\n                  <div class="card-body">\n                    <span class="h3 text-muted">Enter Student ID</span>\n                    <input type="text" class="form-control mt-4 mb-5" required=true id="studentID_id" name="studentID" placeholder="Student ID">\n                    <button type="submit" class="btn btn-submit" id="loginButton">Sign In</button>\n                  </div>\n                </div>\n              </form>\n            </div>\n        </div>\n  </div>\n\n    \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/poll/templates/current.getlogin.html", "uri": "current.getlogin.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "51": 26, "57": 3, "68": 5, "77": 5, "78": 10, "79": 10, "80": 10, "81": 10, "87": 81}}
__M_END_METADATA
"""
