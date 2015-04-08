# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428165730.454385
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/quantity.html'
_template_uri = 'quantity.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\t<div id="quantity_container" align="center">\r\n\t\t\t<form id="quantityform" method="POST" action="/shoppingcart.add/')
        __M_writer(str(request.urlparams[0]))
        __M_writer('">\r\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t\t\t<div align="center"><input id="cart" type="submit" class="btn btn-primary"/></div>\r\n\t\t\t</form>\r\n\t\t</div>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/quantity.html", "uri": "quantity.html", "line_map": {"65": 59, "59": 7, "36": 1, "57": 6, "55": 3, "56": 6, "41": 12, "58": 7, "27": 0, "47": 3}}
__M_END_METADATA
"""
