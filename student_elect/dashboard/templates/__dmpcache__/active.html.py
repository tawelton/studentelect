# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552325821.158458
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/active.html'
_template_uri = 'active.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_content']


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
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_content'):
            context['self'].page_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_content():
            return render_page_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="row">\n\n    <div class="col-xl-3 col-lg-4 col-md-4">\n      <div class="card">\n        <div class="card-body">\n          <h4 class="card-title poll-heading">Student Body Officers</h4>\n          <p class="card-category">\n            Number of votes: <span class="text-success">423</span>\n          </p>\n        </div>\n        <div class="card-footer">\n          <div class="stats">\n            <i class="material-icons">access_time</i> Current round will finish on 3/15/19\n          </div>\n        </div>\n      </div>\n    </div>\n\n    <div class="col-xl-3 col-lg-4 col-md-4">\n        <div class="card">\n          <div class="card-body">\n            <h4 class="card-title poll-heading">Senior Class Officers</h4>\n            <p class="card-category mb-2">\n              Number of votes: <span class="text-success">423</span>\n            </p>\n            <button class="btn btn-sm btn-outline-warning">Edit</button>\n          </div>\n          <div class="card-footer outline-top">\n            <div class="stats">\n              <i class="material-icons">access_time</i> Current round will finish on 3/15/19\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class="col-xl-3 col-lg-4 col-md-4">\n          <div class="card">\n            <div class="card-body">\n              <h4 class="card-title poll-heading">Junior Class Officers</h4>\n              <p class="card-category">\n                Number of votes: <span class="text-success">423</span>\n              </p>\n              <p class="card-category">\n                  <button class="btn btn-outline-warning">Edit</button>\n                </p>\n            </div>\n            <div class="card-footer">\n              <div class="stats">\n                <i class="material-icons">access_time</i> Current round will finish on 3/15/19\n              </div>\n            </div>\n          </div>\n        </div>\n\n  </div>\n  <div class="row">\n    <div class="col-lg-6 col-md-12">\n      <div class="card">\n        <div class="card-header card-header-tabs card-header-primary">\n          <div class="nav-tabs-navigation">\n            <div class="nav-tabs-wrapper">\n              <span class="nav-tabs-title">Tasks:</span>\n              <ul class="nav nav-tabs" data-tabs="tabs">\n                <li class="nav-item">\n                  <a class="nav-link active" href="#profile" data-toggle="tab">\n                    <i class="material-icons">bug_report</i> Bugs\n                    <div class="ripple-container"></div>\n                  </a>\n                </li>\n                <li class="nav-item">\n                  <a class="nav-link" href="#messages" data-toggle="tab">\n                    <i class="material-icons">code</i> Website\n                    <div class="ripple-container"></div>\n                  </a>\n                </li>\n                <li class="nav-item">\n                  <a class="nav-link" href="#settings" data-toggle="tab">\n                    <i class="material-icons">cloud</i> Server\n                    <div class="ripple-container"></div>\n                  </a>\n                </li>\n              </ul>\n            </div>\n          </div>\n        </div>\n        <div class="card-body">\n          <div class="tab-content">\n            <div class="tab-pane active" id="profile">\n              <table class="table">\n                <tbody>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="" checked>\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Sign contract for "What are conference organizers afraid of?"</td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="">\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Lines From Great Russian Literature? Or E-mails From My Boss?</td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="">\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit\n                    </td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="" checked>\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Create 4 Invisible User Experiences you Never Knew About</td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                </tbody>\n              </table>\n            </div>\n            <div class="tab-pane" id="messages">\n              <table class="table">\n                <tbody>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="" checked>\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit\n                    </td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="">\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Sign contract for "What are conference organizers afraid of?"</td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                </tbody>\n              </table>\n            </div>\n            <div class="tab-pane" id="settings">\n              <table class="table">\n                <tbody>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="">\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Lines From Great Russian Literature? Or E-mails From My Boss?</td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="" checked>\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit\n                    </td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                  <tr>\n                    <td>\n                      <div class="form-check">\n                        <label class="form-check-label">\n                          <input class="form-check-input" type="checkbox" value="" checked>\n                          <span class="form-check-sign">\n                            <span class="check"></span>\n                          </span>\n                        </label>\n                      </div>\n                    </td>\n                    <td>Sign contract for "What are conference organizers afraid of?"</td>\n                    <td class="td-actions text-right">\n                      <button type="button" rel="tooltip" title="Edit Task" class="btn btn-primary btn-link btn-sm">\n                        <i class="material-icons">edit</i>\n                      </button>\n                      <button type="button" rel="tooltip" title="Remove" class="btn btn-danger btn-link btn-sm">\n                        <i class="material-icons">close</i>\n                      </button>\n                    </td>\n                  </tr>\n                </tbody>\n              </table>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n    <div class="col-lg-6 col-md-12">\n      <div class="card">\n        <div class="card-header card-header-warning">\n          <h4 class="card-title">Employees Stats</h4>\n          <p class="card-category">New employees on 15th September, 2016</p>\n        </div>\n        <div class="card-body table-responsive">\n          <table class="table table-hover">\n            <thead class="text-warning">\n              <th>ID</th>\n              <th>Name</th>\n              <th>Salary</th>\n              <th>Country</th>\n            </thead>\n            <tbody>\n              <tr>\n                <td>1</td>\n                <td>Dakota Rice</td>\n                <td>$36,738</td>\n                <td>Niger</td>\n              </tr>\n              <tr>\n                <td>2</td>\n                <td>Minerva Hooper</td>\n                <td>$23,789</td>\n                <td>Curaçao</td>\n              </tr>\n              <tr>\n                <td>3</td>\n                <td>Sage Rodriguez</td>\n                <td>$56,142</td>\n                <td>Netherlands</td>\n              </tr>\n              <tr>\n                <td>4</td>\n                <td>Philip Chaney</td>\n                <td>$38,735</td>\n                <td>Korea, South</td>\n              </tr>\n            </tbody>\n          </table>\n        </div>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/active.html", "uri": "active.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 350, "47": 3, "53": 3, "59": 53}}
__M_END_METADATA
"""