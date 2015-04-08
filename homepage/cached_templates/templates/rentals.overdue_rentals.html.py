# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428166419.545697
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/rentals.overdue_rentals.html'
_template_uri = 'rentals.overdue_rentals.html'
_source_encoding = 'ascii'
import os, os.path, re
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        userlist = context.get('userlist', UNDEFINED)
        latelist = context.get('latelist', UNDEFINED)
        latesixtylist = context.get('latesixtylist', UNDEFINED)
        latethirtylist = context.get('latethirtylist', UNDEFINED)
        lateninetylist = context.get('lateninetylist', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')

        import homepage.models as hmod
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['hmod'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        len = context.get('len', UNDEFINED)
        userlist = context.get('userlist', UNDEFINED)
        latelist = context.get('latelist', UNDEFINED)
        latesixtylist = context.get('latesixtylist', UNDEFINED)
        latethirtylist = context.get('latethirtylist', UNDEFINED)
        lateninetylist = context.get('lateninetylist', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t')

        x = 0
                
        
        __M_writer('\r\n')
        if len(latelist) > 0:
            __M_writer('\t\t<div class="titlebar">\r\n\t\t\t<h4>Items that are between 0 and 30 days late</h4>\r\n\t\t</div>\r\n\t\t<table class="table table-striped">\r\n')
            for late in latelist:
                __M_writer('\t\t\t\t')

                x = x + 1
                                                
                
                __M_writer('\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td>')
                __M_writer(str(late.name))
                __M_writer('</td>\r\n\t\t\t\t\t<td>')
                __M_writer(str(userlist[x]))
                __M_writer('\r\n\t\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n')
        __M_writer('\t\r\n')
        if len(latethirtylist) > 0:
            __M_writer('\t<div class="titlebar">\r\n\t\t<h4>Items that are between 30 and 60 days late</h4>\r\n\t</div>\r\n\t<table class="table table-striped">\r\n')
            for late in latethirtylist:
                __M_writer('\t\t\t')

                x = x + 1
                                        
                
                __M_writer('\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
                __M_writer(str(late.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(userlist[x]))
                __M_writer('\r\n\t\t\t</tr>\r\n')
            __M_writer('\t</table>\r\n')
        __M_writer('\r\n')
        if len(latesixtylist) > 0:
            __M_writer('\t\t<div class="titlebar">\r\n\t\t\t<h4>Items that are between 60 and 90 days late</h4>\r\n\t\t</div>\r\n\t\t<table class="table table-striped">\r\n')
            for late in latesixtylist:
                __M_writer('\t\t\t\t')

                x = x + 1
                                                
                
                __M_writer('\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td>')
                __M_writer(str(late.name))
                __M_writer('</td>\r\n\t\t\t\t\t<td>')
                __M_writer(str(userlist[x]))
                __M_writer('\r\n\t\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n')
        __M_writer('\r\n')
        if len(lateninetylist) > 0:
            __M_writer('\t<div class="titlebar">\r\n\t\t<h4>Items that are more than 90 days late</h4>\r\n\t</div>\r\n\t<table class="table table-striped">\r\n')
            for late in lateninetylist:
                __M_writer('\t\t\t')

                x = x + 1
                                        
                
                __M_writer('\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
                __M_writer(str(late.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(userlist[x]))
                __M_writer('\r\n\t\t\t</tr>\r\n')
            __M_writer('\t</table>\r\n')
        __M_writer('\r\n\t</br></br>\r\n\t<a href="/homepage/rentals.email_late/" class="btn btn-primary">Email Notices</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/rentals.overdue_rentals.html", "uri": "rentals.overdue_rentals.html", "line_map": {"128": 69, "129": 71, "130": 71, "131": 72, "132": 72, "133": 75, "134": 77, "140": 134, "27": 0, "40": 1, "41": 2, "47": 4, "57": 6, "69": 6, "70": 7, "74": 9, "75": 10, "76": 11, "77": 15, "78": 16, "79": 16, "83": 18, "84": 20, "85": 20, "86": 21, "87": 21, "88": 24, "89": 26, "90": 27, "91": 28, "92": 32, "93": 33, "94": 33, "98": 35, "99": 37, "100": 37, "101": 38, "102": 38, "103": 41, "104": 43, "105": 44, "106": 45, "107": 49, "108": 50, "109": 50, "113": 52, "114": 54, "115": 54, "116": 55, "117": 55, "118": 58, "119": 60, "120": 61, "121": 62, "122": 66, "123": 67, "124": 67}}
__M_END_METADATA
"""
