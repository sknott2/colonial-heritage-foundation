# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428165265.80771
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/catalog.detail.item.html'
_template_uri = 'catalog.detail.item.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div>\r\n\t\t<h2>')
        __M_writer(str(item.name))
        __M_writer('</h2>\r\n\t\t<div class="img_box">\r\n\t\t\t<img id="detail_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/product_images/')
        __M_writer(str(item.name))
        __M_writer('.jpg" />\r\n\t\t</div>\r\n\t\t<div class="description_box"\r\n\t\t\t<p>\r\n\t\t\t\t')
        __M_writer(str(item.description))
        __M_writer('\r\n\t\t\t</p>\r\n\t\t\t<p>\r\n\t\t\t\tPrice: $')
        __M_writer(str(item.standard_rental_price))
        __M_writer(' per week of use\r\n\t\t\t</p>\r\n\t\t\t\r\n\t\t\t<button data-pid="')
        __M_writer(str( item.id ))
        __M_writer('" id="add_cart" class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/catalog.detail.item.html", "uri": "catalog.detail.item.html", "line_map": {"64": 14, "65": 17, "66": 17, "27": 0, "36": 1, "72": 66, "46": 3, "54": 3, "55": 5, "56": 5, "57": 7, "58": 7, "59": 7, "60": 7, "61": 11, "62": 11, "63": 14}}
__M_END_METADATA
"""
