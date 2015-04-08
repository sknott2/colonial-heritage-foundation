# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428167974.04304
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/receipt_email_template.html'
_template_uri = 'receipt_email_template.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        order = context.get('order', UNDEFINED)
        items = context.get('items', UNDEFINED)
        products = context.get('products', UNDEFINED)
        total = context.get('total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML>\r\n<html>\r\n\t<body>\r\n\t\t<header>Thank you for your purchase with Colonial Heritage Foundation!</header>\r\n\t\t<h4>Order ID: ')
        __M_writer(str( order.id ))
        __M_writer('</h4>\r\n\t\t<h4>Items:</h4>\r\n')
        for product in products:
            __M_writer('\t\t\t\t<h4>')
            __M_writer(str(product.name))
            __M_writer('</h4>\r\n')
        for item in items:
            __M_writer('\t\t\t\t<h4>')
            __M_writer(str(item.name))
            __M_writer('</h4>\r\n')
        __M_writer('\t\t<h4>Total: ')
        __M_writer(str(total))
        __M_writer('</h4>\r\n\t\t<h4>Thanks, the CHF Team</h4>\r\n\r\n\t</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"32": 10, "33": 11, "34": 11, "35": 11, "36": 13, "37": 13, "38": 13, "44": 38, "16": 0, "25": 1, "26": 5, "27": 5, "28": 7, "29": 8, "30": 8, "31": 8}, "source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/receipt_email_template.html", "uri": "receipt_email_template.html"}
__M_END_METADATA
"""
