# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428168006.369669
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/receipt.html'
_template_uri = 'receipt.html'
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
        products = context.get('products', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
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
        products = context.get('products', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Order Complete</h1>\r\n\t<h3>Thank you for shopping with us. You will receive a confirmation email shortly</h3>\r\n\t<p>Items you purchased:</p>\r\n\t<table>\r\n')
        if products:
            for product in products:
                __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>')
                __M_writer(str(product.name))
                __M_writer('</td>\r\n\t\t\t\t\t<td>')
                __M_writer(str(product.current_price))
                __M_writer('</td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\t<p>Items you rented:</p>\r\n\t<table>\r\n')
        if items:
            for item in items:
                __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>')
                __M_writer(str(item.name))
                __M_writer('</td>\r\n\t\t\t\t\t<td>')
                __M_writer(str(item.standard_rental_price))
                __M_writer('</td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 19, "65": 20, "66": 21, "27": 0, "36": 1, "69": 22, "68": 22, "76": 70, "70": 26, "46": 2, "67": 21, "54": 2, "55": 7, "56": 8, "57": 9, "58": 10, "59": 10, "60": 11, "61": 11, "62": 15, "63": 18}, "source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/receipt.html", "uri": "receipt.html"}
__M_END_METADATA
"""
