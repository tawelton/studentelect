# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554064758.409157
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/poll/templates/current.getactivecandidates.html'
_template_uri = 'current.getactivecandidates.html'
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
        candidates = context.get('candidates', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        votelimit = context.get('votelimit', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        candidates = context.get('candidates', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context)
        votelimit = context.get('votelimit', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        from student_elect import settings 
        
        __M_writer('\n\n<div class="container-fluid">\n  <div class="row justify-content-center">\n')
        for candidate in candidates:
            __M_writer('      <div class="col-xl-3 col-lg-3 col-md-4 col-sm-4 col-6 candidate">\n        <div class="card mt-1 candidateCard" data-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.id ))
            __M_writer('" data-checked="unchecked">\n          <div class="card-img-top" style="padding:1rem;">\n            <div class="cand-image" style="background-image: url(\'')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STATIC_URL + settings.MEDIA_URL + str(candidate.imagefile) ))
            __M_writer('\');"></div>\n          </div>\n          <div class="card-body pt-0">\n            <center>\n              <div class="h6 cand-firstname">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.firstname ))
            __M_writer('</div>\n              <div class="h6 cand-lastname">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.lastname ))
            __M_writer('</div>\n            </center>\n          </div>\n        </div>\n      </div>\n')
        __M_writer('  </div>\n  <div class="row justify-content-right">\n    <div class="col-12">\n      <p class="text-muted">You may select up to ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( votelimit ))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'candidates' if votelimit > 1 else 'candidate'))
        __M_writer('</p>\n      <button class="btn btn-primary btn-lg" id="voteButton">Submit Vote</button>\n    </div>\n  </div>\n</div>\n  \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/poll/templates/current.getactivecandidates.html", "uri": "current.getactivecandidates.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 34, "51": 3, "61": 3, "62": 4, "64": 4, "65": 8, "66": 9, "67": 10, "68": 10, "69": 12, "70": 12, "71": 16, "72": 16, "73": 17, "74": 17, "75": 23, "76": 26, "77": 26, "78": 26, "79": 26, "85": 79}}
__M_END_METADATA
"""
