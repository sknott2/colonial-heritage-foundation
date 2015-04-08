# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428535669.935059
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'footer', 'left_side', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left_side():
            return render_left_side(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>s\r\n    <title>Colonial Heritage Foundation</title>\r\n    <meta name="description" content="The Colonial Heritage Foundation is an organization based in Provo, UT that focuses on preserving the heritage of our American forebearers.">\r\n\r\n')
        __M_writer('    <meta property="og:title" content="Colonial Heritage Foundation">\r\n    <meta property="og:type" content="website">\r\n    <meta property="og:url" content="http://colonialheritagefoundation.co">\r\n    <meta property="og:description" content="Check out the awesome events going on at the Colonial Heritage Foundation or stop by to rent colonial era props."/>\r\n\r\n')
        __M_writer('    <meta name="twitter:card" content="summary">\r\n    <meta name="twitter:url" content="http://colonialheritagefoundation.co">\r\n    <meta name="twitter:title" content="Colonial Heritage Foundation">\r\n    <meta name="twitter:description" content="Check out the awesome events going on at the Colonial Heritage Foundation or stop by to rent colonial era props.">\r\n    \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n\r\n    \r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n    \r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n    <div>\r\n      <header>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n      </header>\r\n    </div>\r\n    <div class="container">\r\n      <div class="col-md-2" id="left_menu">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        __M_writer('\r\n      </div>\r\n\r\n      <div class="col-md-10" id="center_content">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(' \r\n      </div>\r\n    </div> \r\n  \r\n    <div>\r\n      <footer>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer(' \r\n      </footer>\r\n    </div>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n    \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n            <div class="col-md-1">\r\n              <img class="navbar_img" src="/static/homepage/media/silouette.png/" class="nav navbar-nav navbar-left">\r\n            </div>\r\n            <div id="navbar-div" class="col-md-9 container-fluid">\r\n                <h3 class="white_text">Colonial Heritage Foundation</h3>\r\n                <h4 class="gray_text">Bringing History to Life</h4>\r\n            </div>\r\n            <div class="col-md-2"\r\n              <ul class="nav navbar-nav navbar-right">\r\n                <li class="navbar-item">\r\n')
        if request.user.is_authenticated():
            __M_writer('                    <a href="/homepage/login.log_out/" class="btn btn-warning login_btn">Log Out</a>\r\n')
        else:
            __M_writer('                    <a href="/homepage/users.create/" class="btn btn-warning login_btn">Create Profile</a>\r\n                    <!--<a href="/homepage/login/" class="btn btn-primary login_btn">Log In</a>-->\r\n                    <button class="btn btn-primary login_btn" id="login">Log In</button>\r\n                    <div class="modal fade" id="modal1" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n                      <div class="modal-dialog">\r\n                        <div class="modal-content">\r\n                          <div class="modal-header">\r\n                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n                            <h4 class="modal-title" id="myModalLabel">Log In</h4>\r\n                          </div>\r\n                          <div class="modal-body">\r\n                          </div>\r\n                          <div class="modal-footer">\r\n                            <a href="/account/password_reset/" class="btn btn-default">Forgot password?</a>\r\n                            <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\r\n                          </div>\r\n                        </div>\r\n                      </div>\r\n                    </div>\r\n')
        __M_writer('                </li>\r\n              </ul\r\n            </div>\r\n\r\n            <!-----------------------------------------------shopping cart----------------------------------------->\r\n            <button class="btn btn-primary" id="shopping_cart">Shopping Cart</button>\r\n\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n          <h6 class="copyright">&copy Colonial Heritage Foundation</h6>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        __M_writer('\r\n          This is the left side menu bar\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n          Site content goes here in sub-templates.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/base.htm", "source_encoding": "ascii", "uri": "base.htm", "line_map": {"65": 98, "133": 127, "70": 106, "71": 110, "72": 110, "73": 110, "109": 90, "79": 44, "16": 4, "18": 0, "86": 44, "87": 55, "88": 56, "89": 57, "90": 58, "91": 78, "97": 104, "34": 2, "35": 4, "36": 5, "103": 104, "40": 5, "41": 15, "42": 21, "43": 27, "44": 28, "45": 28, "46": 29, "47": 29, "48": 38, "49": 38, "50": 38, "115": 90, "55": 85, "121": 96, "60": 92, "127": 96}}
__M_END_METADATA
"""
