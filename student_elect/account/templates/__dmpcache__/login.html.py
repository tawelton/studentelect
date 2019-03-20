# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553111456.535372
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/account/templates/login.html'
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
        def title():
            return render_title(context._locals(__M_locals))
        def pageContent():
            return render_pageContent(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<!-- Default form login -->\n    <div class="card col-xl-4 col-lg-5 col-md-7 col-sm-9 align-self-center">\n        <form method="POST" action="" class="text-center p-4">\n\n            <p class="h4 mb-4">Sign in</p>\n\n            <!-- Email -->\n            <input type="text" id=" ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form['username'].auto_id ))
        __M_writer('" name="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['username'].name))
        __M_writer('" value="" class="form-control mb-4" placeholder="E-mail or Username">\n\n            <!-- Password -->\n            <input type="password" id="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['password'].auto_id ))
        __M_writer('" name="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['password'].name ))
        __M_writer('" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['password'].value ))
        __M_writer('" class="form-control mb-4" placeholder="Password">\n\n            <div class="d-flex justify-content-around">\n                <div>\n                    <!-- Remember me -->\n                    <div class="custom-control custom-checkbox">\n                        <input type="checkbox" class="custom-control-input" id="id_remember_me">\n                        <label class="custom-control-label" for="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['remember_me'].id_for_label ))
        __M_writer('" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form['remember_me'].value ))
        __M_writer('">Remember me</label>\n                    </div>\n                </div>\n                <div>\n                    <!-- Forgot password -->\n                    <a href="/account/reset">Forgot password?</a>\n                </div>\n            </div>\n\n            <!-- Sign in button -->\n            <button class="btn btn-info btn-block my-4" type="submit">Sign in</button>\n\n            <!-- Register -->\n            <p>Not a member?\n                <a href="/account/register">Register</a>\n            </p>\n\n\n        </form>\n    </div>\n\n<!-- Default form login -->\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/account/templates/login.html", "uri": "login.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 3, "50": 48, "56": 3, "62": 3, "68": 5, "76": 5, "77": 14, "78": 14, "79": 14, "80": 14, "81": 17, "82": 17, "83": 17, "84": 17, "85": 17, "86": 17, "87": 24, "88": 24, "89": 24, "90": 24, "96": 90}}
__M_END_METADATA
"""
