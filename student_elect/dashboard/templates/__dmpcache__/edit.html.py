# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553842940.3203242
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/edit.html'
_template_uri = 'edit.html'
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
        poll = context.get('poll', UNDEFINED)
        def page_content():
            return render_page_content(context._locals(__M_locals))
        candidateform = context.get('candidateform', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def pageTitle():
            return render_pageTitle(context._locals(__M_locals))
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
        __M_writer('Edit Poll')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageTitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pageTitle():
            return render_pageTitle(context)
        __M_writer = context.writer()
        __M_writer('Edit Poll')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def page_content():
            return render_page_content(context)
        poll = context.get('poll', UNDEFINED)
        candidateform = context.get('candidateform', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="container-fluid">\n  <div class="row">\n    <div class="col-12">\n          <div id="candidate-container">Loading...</div>\n          <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#candidateModal">Add Candidate</button>\n\n    </div>\n\n\n  </div>\n\n  <form method="POST" action="/dashboard/edit.addcandidate/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( poll ))
        __M_writer('" id="candidateform" enctype="multipart/form-data">\n    <div class="modal fade" id="candidateModal"> \n      <div class="modal-dialog" role="document">\n        <div class="modal-content">\n          <div class="modal-header">\n            <h5 class="modal-title" id="exampleModalLabel">Add Candidate</h5>\n            <button type="button" class="close" data-dismiss="modal" aria-label="Close">\n              <span aria-hidden="true">&times;</span>\n            </button>\n          </div>\n          <div class="modal-body">\n            \n              ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidateform ))
        __M_writer('\n          </div>\n          <div class="modal-footer">\n            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>\n            <button type="submit" class="btn btn-primary" id="candidateSubmit">Add Candidate</button>\n          </div>\n        </div>\n      </div>\n    </div>\n  </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/edit.html", "uri": "edit.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 3, "53": 4, "58": 42, "64": 3, "70": 3, "76": 4, "82": 4, "88": 6, "97": 6, "98": 19, "99": 19, "100": 31, "101": 31, "107": 101}}
__M_END_METADATA
"""
