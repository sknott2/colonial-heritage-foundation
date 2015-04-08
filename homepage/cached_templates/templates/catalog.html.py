# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428165123.166925
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/catalog.html'
_template_uri = '/catalog.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        query_string = context.get('query_string', UNDEFINED)
        items = context.get('items', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        query_string = context.get('query_string', UNDEFINED)
        items = context.get('items', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form class="col-lg-12" role="search">\r\n\t    <div class="form-group">\r\n\t    \t<input type="text" name="q" id="id_q" value="')
        __M_writer(str( query_string ))
        __M_writer('" class="form-control" placeholder="Search">\r\n\t    </div>\r\n\t    <button type="submit" class="btn btn-default">Submit</button>\r\n\t</form>\r\n')
        for product in products:
            __M_writer('\t\t\r\n\t\t<div class="item_container">\r\n\t\t\t<a class="product_link" href="/homepage/catalog.detail/')
            __M_writer(str( product.id ))
            __M_writer('/">\r\n\t\t\t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/product_images/')
            __M_writer(str(product.name))
            __M_writer('.jpg" />\r\n\t\t\t\t<div class="item_title text-muted text-center">')
            __M_writer(str(product.name))
            __M_writer('</div>\r\n\t\t\t</a>\r\n\t\t\t<!--<div class="text-center">\r\n\t\t\t\t<button class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n\t\t\t</div>-->\r\n\t\t</div>\r\n\t\t\r\n')
        __M_writer('\r\n')
        for item in items:
            __M_writer('\t\t\r\n\t\t<div class="item_container">\r\n\t\t\t<a class="product_link" href="/homepage/catalog.item_detail/')
            __M_writer(str( item.id ))
            __M_writer('/">\r\n\t\t\t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/product_images/')
            __M_writer(str(item.name))
            __M_writer('.jpg" />\r\n\t\t\t\t<div class="item_title text-muted text-center">')
            __M_writer(str(item.name))
            __M_writer('</div>\r\n\t\t\t</a>\r\n\t\t\t<!--<div class="text-center">\r\n\t\t\t\t<button class="add_button btn btn-xs btn-warning">Add to Cart</button>\r\n\t\t\t</div>-->\r\n\t\t</div>\r\n\t\t\r\n')
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 14, "65": 14, "66": 15, "67": 15, "68": 15, "69": 15, "70": 16, "71": 16, "72": 24, "73": 25, "74": 26, "75": 28, "76": 28, "77": 29, "78": 29, "79": 29, "80": 29, "81": 30, "82": 30, "83": 38, "89": 83, "27": 0, "38": 1, "39": 2, "49": 4, "59": 4, "60": 7, "61": 7, "62": 11, "63": 12}, "uri": "/catalog.html", "source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/catalog.html"}
__M_END_METADATA
"""
