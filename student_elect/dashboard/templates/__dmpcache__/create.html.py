# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553966965.744707
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/create.html'
_template_uri = 'create.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'pageTitle', 'page_content']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        pollform = context.get('pollform', UNDEFINED)
        def pageTitle():
            return render_pageTitle(context._locals(__M_locals))
        def page_content():
            return render_page_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pageTitle'):
            context['self'].pageTitle(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_content'):
            context['self'].page_content(**pageargs)
        

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
        __M_writer('Create Poll')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageTitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pageTitle():
            return render_pageTitle(context)
        __M_writer = context.writer()
        __M_writer('Create Poll')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        pollform = context.get('pollform', UNDEFINED)
        def page_content():
            return render_page_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n  <div class="container-fluid">\n    <div class="row justify-content-center">\n      \n      <div class="col-lg-6 col-md-6">\n        <div class="card">\n          <div class="card-body">\n            <div class="p-4">\n\n              <div class="create-poll-prompt mb-4">\n                <h3 class="text-left mt-0">Let\'s start off by giving the new poll a name.</h3>\n              </div>\n              <form method="POST">\n              ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( pollform.as_table() ))
        __M_writer('\n\n              <button type="submit" class="btn btn-primary mt-4">Create</button>\n              </form>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/create.html", "uri": "create.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 4, "57": 30, "63": 3, "69": 3, "75": 4, "81": 4, "87": 6, "95": 6, "96": 20, "97": 20, "103": 97}}
__M_END_METADATA
"""
