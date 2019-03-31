# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553966991.176916
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
        def content():
            return render_content(context._locals(__M_locals))
        candidates = context.get('candidates', UNDEFINED)
        poll = context.get('poll', UNDEFINED)
        len = context.get('len', UNDEFINED)
        str = context.get('str', UNDEFINED)
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
        def content():
            return render_content(context)
        candidates = context.get('candidates', UNDEFINED)
        poll = context.get('poll', UNDEFINED)
        len = context.get('len', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        from student_elect import settings 
        
        __M_writer('\n\n<div class="container-fluid">\n    <div class="row">\n')
        if len(candidates) > 0:
            for candidate in candidates:
                __M_writer('        <div class="col-xl-2 col-lg-3 col-md-3 col-sm-4 col-xs-6 candidate">\n          <div class="card mt-1">\n            <div class="card-img-top" style="padding:1rem;">\n              <div class="cand-image" style="background-image: url(\'')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STATIC_URL + settings.MEDIA_URL + str(candidate.imagefile) ))
                __M_writer('\');"></div>\n            </div>\n            <div class="card-body pt-0">\n              <center>\n                <div class="h6 cand-firstname">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.firstname ))
                __M_writer('</div>\n                <div class="h6 cand-lastname">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.lastname ))
                __M_writer('</div>\n                <div class="cand-votes">Votes: ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.vote_set.filter(round=poll.round).count() ))
                __M_writer('</div>\n\n              </center>\n            </div> \n            <div class="close" data-id="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.id ))
                __M_writer('">\n                <i class="material-icons">\n                    close\n                </i>\n            </div>\n          </div>\n        </div>\n')
        else:
            __M_writer('        <div class="col-12">\n          <h5>Add candidates by clicking the "+" button above.</h5>\n        </div>\n')
        __M_writer('  </div>\n</div>\n  \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/edit.getactivecandidates.html", "uri": "edit.getactivecandidates.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 41, "52": 3, "63": 3, "64": 4, "66": 4, "67": 8, "68": 9, "69": 10, "70": 13, "71": 13, "72": 17, "73": 17, "74": 18, "75": 18, "76": 19, "77": 19, "78": 23, "79": 23, "80": 31, "81": 32, "82": 36, "88": 82}}
__M_END_METADATA
"""
