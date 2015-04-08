# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428112696.197449
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/rentals.return_item.html'
_template_uri = 'rentals.return_item.html'
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        agent = context.get('agent', UNDEFINED)
        loaned_list = context.get('loaned_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        agent = context.get('agent', UNDEFINED)
        loaned_list = context.get('loaned_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="col-md-6">\r\n\t\t<table class="table table-striped">\r\n\t\t\t<tr>\r\n\t\t\t\t<td>Item Name</td>\r\n\t\t\t\t<td>Item Rental Price</td>\r\n\t\t\t\t<td>Return</td>\r\n\t\t\t</tr>\r\n')
        for item in loaned_list:
            __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>')
            __M_writer(str( item.name ))
            __M_writer('</td>\r\n\t\t\t\t\t<td>')
            __M_writer(str( item.standard_rental_price ))
            __M_writer('</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a class="btn-xs btn-primary" href="/homepage/rentals.return_rental/')
            __M_writer(str( user.id ))
            __M_writer('/')
            __M_writer(str( agent.id ))
            __M_writer('/')
            __M_writer(str( item.id ))
            __M_writer('/">Return Item</a>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rentals.return_item.html", "source_encoding": "ascii", "line_map": {"64": 16, "65": 16, "66": 16, "27": 0, "68": 16, "37": 1, "70": 20, "42": 22, "76": 70, "48": 3, "67": 16, "69": 16, "57": 3, "58": 11, "59": 12, "60": 13, "61": 13, "62": 14, "63": 14}, "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/rentals.return_item.html"}
__M_END_METADATA
"""
