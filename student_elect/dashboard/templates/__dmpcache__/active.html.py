# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553968784.927826
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/active.html'
_template_uri = 'active.html'
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
        def page_content():
            return render_page_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        polls = context.get('polls', UNDEFINED)
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
        __M_writer('Active Polls')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageTitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pageTitle():
            return render_pageTitle(context)
        __M_writer = context.writer()
        __M_writer('Active Polls')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def page_content():
            return render_page_content(context)
        polls = context.get('polls', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  ')
        from django.db.models import Count 
        
        __M_writer('\n\n  <div class="container-fluid">\n    <div class="row">\n      \n')
        for poll in polls:
            __M_writer('\n      <div class="col-lg-6 col-md-6">\n        <div class="card mt-0">\n          <div class="card-body">\n              <h3 class="card-title">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( poll.title ))
            __M_writer('</h3>\n            <div class="row">\n              <div class="col-lg-12 col-md-12 table-responsive mt-3">\n                  <table class="table table-hover">\n                      <h6 class="h6 text-left mb-0 ml-2">Top 5</h6>\n                      <thead class="text-primary">\n                        <th>Name</th>\n                        <th class="text-center">Votes</th>\n                      </thead>\n                      <tbody>\n\n')
            for candidate in poll.candidate_set.filter(status='A').annotate(num_votes=Count('vote')).order_by('-num_votes')[:5]:
                __M_writer('\n                        <tr>\n                          <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.firstname + " " + candidate.lastname ))
                __M_writer('</td>\n                          <td class="text-center">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( candidate.vote_set.filter(round=poll.round).count() ))
                __M_writer('</td>\n                        </tr>\n                        \n')
            __M_writer('                      </tbody>\n                    </table>\n              </div>\n            </div>\n          </div>\n          <a class="btn btn-block btn-warning btn-round btn-just-icon edit-button" href="/dashboard/edit/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( poll.id ))
            __M_writer('"><i class="material-icons">edit</i></a>\n        </div>\n      </div>\n\n')
        __M_writer('\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/active.html", "uri": "active.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 4, "57": 50, "63": 3, "69": 3, "75": 4, "81": 4, "87": 6, "95": 6, "96": 8, "98": 8, "99": 13, "100": 14, "101": 18, "102": 18, "103": 29, "104": 30, "105": 32, "106": 32, "107": 33, "108": 33, "109": 37, "110": 42, "111": 42, "112": 47, "118": 112}}
__M_END_METADATA
"""
