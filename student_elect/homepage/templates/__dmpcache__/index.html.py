# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554066478.533171
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/homepage/templates/index.html'
_template_uri = 'index.html'
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
    return runtime._inherit_from(context, '/poll/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def page_content():
            return render_page_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_content():
            return render_page_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container-fluid fullscreen h-100">\n    <div class="row pt-5 h-100 justify-content-center">\n        <div class="col-lg-8 col-md-8 col-sm-10 text-center animated">\n            <h1 class="">Student Elect</h1>\n\n            <div id="interface">\n\n                <div class="container">\n                    <div class="row justify-content-center">\n                        <div class="col-lg-8 col-md-10 col-sm-12 m-3">\n                            <div class="h3 text-primary mb-4">Under construction, check back later!</div>\n                            <div class="h6 text-muted">If you already have an account, here\'s a link to your dashboard</div>\n                            <a class="btn btn-submit m-0" href="/dashboard/">\n                                    Dashboard\n                            </a>\n                        </div>\n                    </div>\n                </div>\n\n            </div> \n\n        </div>            \n    </div>\n</div>\n    \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 3, "48": 34, "54": 3, "60": 3, "66": 5, "72": 5, "78": 72}}
__M_END_METADATA
"""
