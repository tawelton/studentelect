# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553060855.6843789
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
        def pageTitle():
            return render_pageTitle(context._locals(__M_locals))
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
        def page_content():
            return render_page_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="row">\n    <div class="col-lg-6 col-md-6">\n      <div class="card">\n        <div class="card-header card-header-primary">\n          <h3 class="card-title">Student Body Officers</h3>\n        </div>\n        <div class="card-body">\n          <div class="row">\n            <div class="col-lg-12 col-md-12 table-responsive">\n                <table class="table table-hover">\n                    <thead class="text-warning">\n                      <th>Rank</th>\n                      <th>Name</th>\n                      <th>Votes</th>\n                    </thead>\n                    <tbody>\n                      <tr>\n                        <td>1</td>\n                        <td>Dakota Rice</td>\n                        <td>476</td>\n                      </tr>\n                      <tr>\n                        <td>2</td>\n                        <td>Minerva Hooper</td>\n                        <td>450</td>\n                      </tr>\n                      <tr>\n                        <td>3</td>\n                        <td>Sage Rodriguez</td>\n                        <td>409</td>\n                      </tr>\n                      <tr>\n                        <td>4</td>\n                        <td>Philip Chaney</td>\n                        <td>387</td>\n                      </tr>\n                      <tr>\n                          <td>5</td>\n                          <td>David Fraire</td>\n                          <td>358</td>\n                        </tr>\n                    </tbody>\n                  </table>\n            </div>\n            <div class="col-lg-12 col-md-12">\n              <div class="row no-gutters justify-content-center">\n                <div class="col-xl-4 col-lg-6 col-md-6 p-1">\n                  <a class="btn btn-block btn-info" href="/dashboard/details/">Details</a>\n                </div>\n                <div class="col-xl-4 col-lg-6 col-md-6 p-1">\n                  <a class="btn btn-block btn-warning" href="/dashboard/edit">Edit</a>\n                </div>\n              </div>\n            </div>\n          </div>\n          \n        </div>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/active.html", "uri": "active.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 3, "50": 4, "55": 67, "61": 3, "67": 3, "73": 4, "79": 4, "85": 6, "91": 6, "97": 91}}
__M_END_METADATA
"""
