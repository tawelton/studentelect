# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553277445.965717
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content', 'pageContent']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def pageContent():
            return render_pageContent(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pageContent():
            return render_pageContent(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <div class="container">\n            <div class="row justify-content-center" style="height: 100vh">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pageContent'):
            context['self'].pageContent(**pageargs)
        

        __M_writer('\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pageContent():
            return render_pageContent(context)
        __M_writer = context.writer()
        __M_writer('PUT CONTENT HERE')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/account/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 11, "49": 3, "57": 3, "62": 7, "68": 7, "74": 7, "80": 74}}
__M_END_METADATA
"""
