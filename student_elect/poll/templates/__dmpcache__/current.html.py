# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553998042.4542232
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/poll/templates/current.html'
_template_uri = 'current.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'page_content']


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
        def title():
            return render_title(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        polls = context.get('polls', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_content():
            return render_page_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( user.organization ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_content():
            return render_page_content(context)
        polls = context.get('polls', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container-fluid fullscreen h-100">\n    <div class="row pt-5 h-100 justify-content-center">\n        <div class="col-lg-8 col-md-8 col-sm-10 text-center animated">\n            <h1 class="">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( user.organization ))
        __M_writer('</h1>\n\n            <div id="interface">\n\n                <div class="container">\n')
        for poll in polls:
            __M_writer('                        <div class="row justify-content-center">\n                            <div class="col-lg-8 col-md-10 col-sm-12 m-3">\n                                <button class="btn btn-lg btn-block btn-primary m-0 pollSelect" data-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( poll.id ))
            __M_writer('">\n                                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( poll.title ))
            __M_writer('\n                                </button>\n                            </div>\n                        </div>\n')
        __M_writer('                </div>\n\n            </div> \n\n        </div>            \n    </div>\n</div>\n    \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/poll/templates/current.html", "uri": "current.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "51": 34, "57": 3, "65": 3, "71": 5, "80": 5, "81": 10, "82": 10, "83": 15, "84": 16, "85": 18, "86": 18, "87": 19, "88": 19, "89": 24, "95": 89}}
__M_END_METADATA
"""
