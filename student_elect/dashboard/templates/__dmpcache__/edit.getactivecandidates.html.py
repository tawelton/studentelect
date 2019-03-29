# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553842134.9180071
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/edit.getactivecandidates.html'
_template_uri = 'edit.getactivecandidates.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


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
        self = context.get('self', UNDEFINED)
        candidates = context.get('candidates', UNDEFINED)
        str = context.get('str', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        candidates = context.get('candidates', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        from student_elect import settings 
        
        __M_writer('\n\n<div class="container">\n    <div class="row">\n')
        for candidate in candidates:
            __M_writer('      <div class="col-xl-2 col-lg-3 col-md-3 col-sm-4 col-xs-6 candidate">\n        <div class="card mt-1">\n          <div class="card-img-top" style="padding:1rem;">\n            <div class="cand-image" style="background-image: url(\'')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STATIC_URL + settings.MEDIA_URL + str(candidate.imagefile) ))
            __M_writer('\');"></div>\n          </div>\n          <div class="card-body pt-0">\n            <center>\n              <div class="h6 cand-firstname">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.firstname ))
            __M_writer('</div>\n              <div class="h6 cand-lastname">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.lastname ))
            __M_writer('</div>\n            </center>\n          </div>\n          <div class="close" data-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.id ))
            __M_writer('">\n              <i class="material-icons">\n                  close\n              </i>\n          </div>\n        </div>\n      </div>\n')
        __M_writer('  </div>\n</div>\n  \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/edit.getactivecandidates.html", "uri": "edit.getactivecandidates.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 33, "50": 3, "59": 3, "60": 4, "62": 4, "63": 8, "64": 9, "65": 12, "66": 12, "67": 16, "68": 16, "69": 17, "70": 17, "71": 20, "72": 20, "73": 28, "79": 73}}
__M_END_METADATA
"""
