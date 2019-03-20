# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551732339.179472
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/student_elect/account/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'pageContent']


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
        def pageContent():
            return render_pageContent(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pageContent'):
            context['self'].pageContent(**pageargs)
        

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
        __M_writer('Sign In')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pageContent():
            return render_pageContent(context)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<!-- Default form login -->\n<form method="POST" class="text-center border border-light p-5">\n\n    <p class="h4 mb-4">Sign in</p>\n\n    <!-- Email -->\n    <input type="text" id=" ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form['username'].auto_id ))
        __M_writer('" name="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['username'].name))
        __M_writer('" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['username'].cleaned_data.get('username') ))
        __M_writer('" class="form-control mb-4" placeholder="E-mail or Username">\n\n    <!-- Password -->\n    <input type="password" id="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['password'].auto_id ))
        __M_writer('" name="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['password'].name ))
        __M_writer('" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['password'].value ))
        __M_writer('" class="form-control mb-4" placeholder="Password">\n\n    <div class="d-flex justify-content-around">\n        <div>\n            <!-- Remember me -->\n            <div class="custom-control custom-checkbox">\n                <input type="checkbox" class="custom-control-input" id="id_remember_me">\n                <label class="custom-control-label" for="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['remember_me'].id_for_label ))
        __M_writer('" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['remember_me'].value ))
        __M_writer('">Remember me</label>\n            </div>\n        </div>\n        <div>\n            <!-- Forgot password -->\n            <a href="/account/reset">Forgot password?</a>\n        </div>\n    </div>\n\n    <!-- Sign in button -->\n    <button class="btn btn-info btn-block my-4" type="submit">Sign in</button>\n\n    <!-- Register -->\n    <p>Not a member?\n        <a href="/account/register">Register</a>\n    </p>\n\n\n</form>\n<!-- Default form login -->\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/student_elect/account/templates/login.html", "uri": "login.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 3, "50": 45, "56": 3, "62": 3, "68": 5, "76": 5, "77": 13, "78": 13, "79": 13, "80": 13, "81": 13, "82": 13, "83": 16, "84": 16, "85": 16, "86": 16, "87": 16, "88": 16, "89": 23, "90": 23, "91": 23, "92": 23, "98": 92}}
__M_END_METADATA
"""
