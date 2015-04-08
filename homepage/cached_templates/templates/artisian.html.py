# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428168625.810529
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/artisian.html'
_template_uri = 'artisian.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        areaproducts = context.get('areaproducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        areaproducts = context.get('areaproducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n        <div class="row">\n')
        for AreaProduct in areaproducts:
            __M_writer('            <div class="col-sm-4">\n                <div class="thumbnail product" id="thumbnail">\n                    <div class="item_container text-center">\n                        <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/artisian/')
            __M_writer(str( AreaProduct.id ))
            __M_writer('.jpg" style="width: 150px; height: 150px;" alt="Image not available"/>\n                        <div class="caption" style="text-align:center;">\n                            <h3 class="name">')
            __M_writer(str( AreaProduct.name ))
            __M_writer('</h3>\n                            <p class="description"> ')
            __M_writer(str( AreaProduct.description ))
            __M_writer('</p>\n                            <p>Price range: ')
            __M_writer(str( AreaProduct.low_price ))
            __M_writer(' to ')
            __M_writer(str( AreaProduct.high_price ))
            __M_writer(' </p>\n                        </div>\n                    </div>\n                </div>\n            </div>\n')
        __M_writer('        </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 14, "65": 15, "66": 15, "27": 0, "36": 1, "69": 21, "68": 15, "75": 69, "46": 3, "67": 15, "54": 3, "55": 7, "56": 8, "57": 11, "58": 11, "59": 11, "60": 11, "61": 13, "62": 13, "63": 14}, "source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/artisian.html", "uri": "artisian.html"}
__M_END_METADATA
"""
