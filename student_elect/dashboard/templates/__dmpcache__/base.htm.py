# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553060345.436204
_enable_loop = True
_template_filename = '/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'pageTitle', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def pageTitle():
            return render_pageTitle(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <meta charset="utf-8" />\n        <link rel="apple-touch-icon" sizes="76x76" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/media/theme/apple-icon.png">\n        <link rel="icon" type="image/png" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/media/theme/favicon.png">\n        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />\n        <title>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(' - StudentElect\n        </title>\n        <meta content=\'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no\' name=\'viewport\' />\n        <!--     Fonts and icons     -->\n        <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Roboto+Slab:400,700|Material+Icons" />\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css">\n        <!-- CSS Files -->\n        <link href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/styles/material-dashboard.css" rel="stylesheet" />\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body class="">\n        <div class="wrapper ">\n          <div class="sidebar" data-color="purple" data-background-color="white" data-image="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/media/theme/sidebar-1.jpg">\n            <!--\n              Tip 1: You can change the color of the sidebar using: data-color="purple | azure | green | orange | danger"\n      \n              Tip 2: you can also add an image using data-image tag\n          -->\n            <div class="logo">\n              <a href="http://www.creative-tim.com" class="simple-text logo-normal">\n                Student Elect\n              </a>\n            </div>\n            <div class="sidebar-wrapper">\n              <ul class="nav">\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'create' else '' ))
        __M_writer('">\n                  <a class="nav-link" href="/dashboard/create">\n                    <i class="material-icons">add_box</i>\n                    <p>Create Poll</p>\n                  </a>\n                </li>\n                <hr/>\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'active' else '' ))
        __M_writer('">\n                  <a class="nav-link" href="/dashboard/active">\n                    <i class="material-icons">list</i>\n                    <p>Active Polls</p>\n                  </a>\n                </li>\n                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'completed' else '' ))
        __M_writer('">\n                  <a class="nav-link" href="/dashboard/completed">\n                    <i class="material-icons">done</i>\n                    <p>Completed Polls</p>\n                  </a>\n                </li>\n                <li class="nav-item active-pro ">\n                  <a class="nav-link" href="./upgrade.html">\n                    <i class="material-icons">unarchive</i>\n                    <p>Upgrade to PRO</p>\n                  </a>\n                </li>\n              </ul>\n            </div>\n          </div>\n          <div class="main-panel">\n            <!-- Navbar -->\n            <nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ">\n              <div class="container-fluid">\n                <div class="navbar-wrapper">\n                  <a class="navbar-brand" href="#pablo">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pageTitle'):
            context['self'].pageTitle(**pageargs)
        

        __M_writer('</a>\n                </div>\n                <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">\n                  <span class="sr-only">Toggle navigation</span>\n                  <span class="navbar-toggler-icon icon-bar"></span>\n                  <span class="navbar-toggler-icon icon-bar"></span>\n                  <span class="navbar-toggler-icon icon-bar"></span>\n                </button>\n                <div class="collapse navbar-collapse justify-content-end">\n                  <form class="navbar-form">\n                    <div class="input-group no-border">\n                      <input type="text" value="" class="form-control" placeholder="Search...">\n                      <button type="submit" class="btn btn-white btn-round btn-just-icon">\n                        <i class="material-icons">search</i>\n                        <div class="ripple-container"></div>\n                      </button>\n                    </div>\n                  </form>\n                  <ul class="navbar-nav">\n                    <li class="nav-item">\n                      <a class="nav-link" href="#pablo">\n                        <i class="material-icons">dashboard</i>\n                        <p class="d-lg-none d-md-block">\n                          Stats\n                        </p>\n                      </a>\n                    </li>\n                    <li class="nav-item dropdown">\n                      <a class="nav-link" href="http://example.com" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                        <i class="material-icons">notifications</i>\n                        <span class="notification">5</span>\n                        <p class="d-lg-none d-md-block">\n                          Some Actions\n                        </p>\n                      </a>\n                      <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">\n                        <a class="dropdown-item" href="#">Mike John responded to your email</a>\n                        <a class="dropdown-item" href="#">You have 5 new tasks</a>\n                        <a class="dropdown-item" href="#">You\'re now friend with Andrew</a>\n                        <a class="dropdown-item" href="#">Another Notification</a>\n                        <a class="dropdown-item" href="#">Another One</a>\n                      </div>\n                    </li>\n                    <li class="nav-item dropdown">\n                      <a class="nav-link" href="#pablo" id="navbarDropdownProfile" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n                        <i class="material-icons">person</i>\n                        <p class="d-lg-none d-md-block">\n                          Account\n                        </p>\n                      </a>\n                      <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownProfile">\n                        <a class="dropdown-item" href="#">Profile</a>\n                        <a class="dropdown-item" href="#">Settings</a>\n                        <div class="dropdown-divider"></div>\n                        <a class="dropdown-item" href="#">Log out</a>\n                      </div>\n                    </li>\n                  </ul>\n                </div>\n              </div>\n            </nav>\n            <!-- End Navbar -->\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n          </div>\n        </div>\n        <!--   Core JS Files   -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/core/jquery.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/core/popper.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/core/bootstrap-material-design.min.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/perfect-scrollbar.jquery.min.js"></script>\n        <!-- Plugin for the momentJs  -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/moment.min.js"></script>\n        <!--  Plugin for Sweet Alert -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/sweetalert2.js"></script>\n        <!-- Forms Validations Plugin -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/jquery.validate.min.js"></script>\n        <!-- Plugin for the Wizard, full documentation here: https://github.com/VinceG/twitter-bootstrap-wizard -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/jquery.bootstrap-wizard.js"></script>\n        <!--\tPlugin for Select, full documentation here: http://silviomoreto.github.io/bootstrap-select -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/bootstrap-selectpicker.js"></script>\n        <!--  Plugin for the DateTimePicker, full documentation here: https://eonasdan.github.io/bootstrap-datetimepicker/ -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/bootstrap-datetimepicker.min.js"></script>\n        <!--  DataTables.net Plugin, full documentation here: https://datatables.net/  -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/jquery.dataTables.min.js"></script>\n        <!--\tPlugin for Tags, full documentation here: https://github.com/bootstrap-tagsinput/bootstrap-tagsinputs  -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/bootstrap-tagsinput.js"></script>\n        <!-- Plugin for Fileupload, full documentation here: http://www.jasny.net/bootstrap/javascript/#fileinput -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/jasny-bootstrap.min.js"></script>\n        <!--  Full Calendar Plugin, full documentation here: https://github.com/fullcalendar/fullcalendar    -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/fullcalendar.min.js"></script>\n        <!-- Vector Map plugin, full documentation here: http://jvectormap.com/documentation/ -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/jquery-jvectormap.js"></script>\n        <!--  Plugin for the Sliders, full documentation here: http://refreshless.com/nouislider/ -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/nouislider.min.js"></script>\n        <!-- Include a polyfill for ES6 Promises (optional) for IE11, UC Browser and Android browser support SweetAlert -->\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/core-js/2.4.1/core.js"></script>\n        <!-- Library for adding dinamically elements -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/arrive.min.js"></script>\n        <!--  Google Maps Plugin    -->\n        <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY_HERE"></script>\n        <!-- Chartist JS -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/chartist.min.js"></script>\n        <!--  Notifications Plugin    -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/plugins/bootstrap-notify.js"></script>\n        <!-- Control Center for Material Dashboard: parallax effects, scripts for the example pages etc -->\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('dashboard/scripts/material-dashboard.js?v=2.1.1" type="text/javascript"></script>\n\n        <script>\n          $(document).ready(function() {\n            $().ready(function() {\n              $sidebar = $(\'.sidebar\');\n      \n              $sidebar_img_container = $sidebar.find(\'.sidebar-background\');\n      \n              $full_page = $(\'.full-page\');\n      \n              $sidebar_responsive = $(\'body > .navbar-collapse\');\n      \n              window_width = $(window).width();\n      \n              fixed_plugin_open = $(\'.sidebar .sidebar-wrapper .nav li.active a p\').html();\n      \n              if (window_width > 767 && fixed_plugin_open == \'Dashboard\') {\n                if ($(\'.fixed-plugin .dropdown\').hasClass(\'show-dropdown\')) {\n                  $(\'.fixed-plugin .dropdown\').addClass(\'open\');\n                }\n      \n              }\n      \n              $(\'.fixed-plugin a\').click(function(event) {\n                // Alex if we click on switch, stop propagation of the event, so the dropdown will not be hide, otherwise we set the  section active\n                if ($(this).hasClass(\'switch-trigger\')) {\n                  if (event.stopPropagation) {\n                    event.stopPropagation();\n                  } else if (window.event) {\n                    window.event.cancelBubble = true;\n                  }\n                }\n              });\n      \n              $(\'.fixed-plugin .active-color span\').click(function() {\n                $full_page_background = $(\'.full-page-background\');\n      \n                $(this).siblings().removeClass(\'active\');\n                $(this).addClass(\'active\');\n      \n                var new_color = $(this).data(\'color\');\n      \n                if ($sidebar.length != 0) {\n                  $sidebar.attr(\'data-color\', new_color);\n                }\n      \n                if ($full_page.length != 0) {\n                  $full_page.attr(\'filter-color\', new_color);\n                }\n      \n                if ($sidebar_responsive.length != 0) {\n                  $sidebar_responsive.attr(\'data-color\', new_color);\n                }\n              });\n      \n              $(\'.fixed-plugin .background-color .badge\').click(function() {\n                $(this).siblings().removeClass(\'active\');\n                $(this).addClass(\'active\');\n      \n                var new_color = $(this).data(\'background-color\');\n      \n                if ($sidebar.length != 0) {\n                  $sidebar.attr(\'data-background-color\', new_color);\n                }\n              });\n      \n              $(\'.fixed-plugin .img-holder\').click(function() {\n                $full_page_background = $(\'.full-page-background\');\n      \n                $(this).parent(\'li\').siblings().removeClass(\'active\');\n                $(this).parent(\'li\').addClass(\'active\');\n      \n      \n                var new_image = $(this).find("img").attr(\'src\');\n      \n                if ($sidebar_img_container.length != 0 && $(\'.switch-sidebar-image input:checked\').length != 0) {\n                  $sidebar_img_container.fadeOut(\'fast\', function() {\n                    $sidebar_img_container.css(\'background-image\', \'url("\' + new_image + \'")\');\n                    $sidebar_img_container.fadeIn(\'fast\');\n                  });\n                }\n      \n                if ($full_page_background.length != 0 && $(\'.switch-sidebar-image input:checked\').length != 0) {\n                  var new_image_full_page = $(\'.fixed-plugin li.active .img-holder\').find(\'img\').data(\'src\');\n      \n                  $full_page_background.fadeOut(\'fast\', function() {\n                    $full_page_background.css(\'background-image\', \'url("\' + new_image_full_page + \'")\');\n                    $full_page_background.fadeIn(\'fast\');\n                  });\n                }\n      \n                if ($(\'.switch-sidebar-image input:checked\').length == 0) {\n                  var new_image = $(\'.fixed-plugin li.active .img-holder\').find("img").attr(\'src\');\n                  var new_image_full_page = $(\'.fixed-plugin li.active .img-holder\').find(\'img\').data(\'src\');\n      \n                  $sidebar_img_container.css(\'background-image\', \'url("\' + new_image + \'")\');\n                  $full_page_background.css(\'background-image\', \'url("\' + new_image_full_page + \'")\');\n                }\n      \n                if ($sidebar_responsive.length != 0) {\n                  $sidebar_responsive.css(\'background-image\', \'url("\' + new_image + \'")\');\n                }\n              });\n      \n              $(\'.switch-sidebar-image input\').change(function() {\n                $full_page_background = $(\'.full-page-background\');\n      \n                $input = $(this);\n      \n                if ($input.is(\':checked\')) {\n                  if ($sidebar_img_container.length != 0) {\n                    $sidebar_img_container.fadeIn(\'fast\');\n                    $sidebar.attr(\'data-image\', \'#\');\n                  }\n      \n                  if ($full_page_background.length != 0) {\n                    $full_page_background.fadeIn(\'fast\');\n                    $full_page.attr(\'data-image\', \'#\');\n                  }\n      \n                  background_image = true;\n                } else {\n                  if ($sidebar_img_container.length != 0) {\n                    $sidebar.removeAttr(\'data-image\');\n                    $sidebar_img_container.fadeOut(\'fast\');\n                  }\n      \n                  if ($full_page_background.length != 0) {\n                    $full_page.removeAttr(\'data-image\', \'#\');\n                    $full_page_background.fadeOut(\'fast\');\n                  }\n      \n                  background_image = false;\n                }\n              });\n      \n              $(\'.switch-sidebar-mini input\').change(function() {\n                $body = $(\'body\');\n      \n                $input = $(this);\n      \n                if (md.misc.sidebar_mini_active == true) {\n                  $(\'body\').removeClass(\'sidebar-mini\');\n                  md.misc.sidebar_mini_active = false;\n      \n                  $(\'.sidebar .sidebar-wrapper, .main-panel\').perfectScrollbar();\n      \n                } else {\n      \n                  $(\'.sidebar .sidebar-wrapper, .main-panel\').perfectScrollbar(\'destroy\');\n      \n                  setTimeout(function() {\n                    $(\'body\').addClass(\'sidebar-mini\');\n      \n                    md.misc.sidebar_mini_active = true;\n                  }, 300);\n                }\n      \n                // we simulate the window Resize so the charts will get updated in realtime.\n                var simulateWindowResize = setInterval(function() {\n                  window.dispatchEvent(new Event(\'resize\'));\n                }, 180);\n      \n                // we stop the simulation of Window Resize after the animations are completed\n                setTimeout(function() {\n                  clearInterval(simulateWindowResize);\n                }, 1000);\n      \n              });\n            });\n          });\n        </script>\n        <script>\n          $(document).ready(function() {\n            // Javascript method\'s body can be found in assets/js/demos.js\n            md.initDashboardPageCharts();\n      \n          });\n        </script>\n      </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pageTitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pageTitle():
            return render_pageTitle(context)
        __M_writer = context.writer()
        __M_writer('INSERT TITLE')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/tannerwelton/Documents/OneDrive - BYU Office 365/Projects/student_elect/student_elect/dashboard/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "32": 2, "33": 8, "34": 8, "35": 9, "36": 9, "41": 12, "42": 19, "43": 19, "44": 22, "45": 23, "46": 23, "47": 28, "48": 28, "49": 41, "50": 41, "51": 48, "52": 48, "53": 54, "54": 54, "59": 74, "64": 136, "65": 140, "66": 140, "67": 141, "68": 141, "69": 142, "70": 142, "71": 143, "72": 143, "73": 145, "74": 145, "75": 147, "76": 147, "77": 149, "78": 149, "79": 151, "80": 151, "81": 153, "82": 153, "83": 155, "84": 155, "85": 157, "86": 157, "87": 159, "88": 159, "89": 161, "90": 161, "91": 163, "92": 163, "93": 165, "94": 165, "95": 167, "96": 167, "97": 171, "98": 171, "99": 175, "100": 175, "101": 177, "102": 177, "103": 179, "104": 179, "110": 12, "121": 74, "127": 74, "133": 136, "144": 133}}
__M_END_METADATA
"""
