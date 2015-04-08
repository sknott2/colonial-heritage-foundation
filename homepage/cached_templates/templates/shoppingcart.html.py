# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428165735.863103
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/shoppingcart.html'
_template_uri = 'shoppingcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


import homepage.models as hmod 

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
        cart_products = context.get('cart_products', UNDEFINED)
        cart_product_size = context.get('cart_product_size', UNDEFINED)
        cart_items = context.get('cart_items', UNDEFINED)
        user = context.get('user', UNDEFINED)
        cart_item_size = context.get('cart_item_size', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('!\r\n\r\n')
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
        cart_products = context.get('cart_products', UNDEFINED)
        cart_product_size = context.get('cart_product_size', UNDEFINED)
        cart_items = context.get('cart_items', UNDEFINED)
        user = context.get('user', UNDEFINED)
        cart_item_size = context.get('cart_item_size', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if cart_product_size > 0:
            __M_writer('\t<h2>Products</h2>\r\n')
        for product in cart_products:
            __M_writer('\t\t<div class="item_div"> \r\n\t\t\t<div class="text">\r\n\t\t\t\t<div id="name">')
            __M_writer(str( product[0] ))
            __M_writer('</div></br>\r\n\t\t\t\t<div id="quantity" class="text-right">')
            __M_writer(str(product[1]))
            __M_writer('</div>\r\n\t\t\t</div>\r\n\r\n\t\t\t<div>\r\n\t\t\t\t<a id="del" href="/homepage/shoppingcart.delete/')
            __M_writer(str(product[0].id))
            __M_writer('" class="btn-xs btn btn-primary">Delete</a>\r\n\t\t\t</div>\r\n\t\t<div>\r\n')
        if cart_item_size > 0:
            __M_writer('\t<h2>Rental Items</h2>\r\n')
        for item in cart_items:
            __M_writer('\t\t')

                        #it = hmod.Item.objects.get(id=item)
                

            __M_writer('\r\n\t\t<div class="item_div">\r\n\t\t\t<div class="text">\r\n\t\t\t\t<div id="name">')
            __M_writer(str( item[0] ))
            __M_writer('</div></br>\r\n\t\t\t</div>\r\n\t\t\t<div>\r\n\t\t\t\t<a id="del" href="/homepage/shoppingcart.delete_item/')
            __M_writer(str( item[0].id ))
            __M_writer('" class="btn-xs btn btn-primary">Delete</a>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        if cart_item_size != 0 or cart_product_size != 0:
            __M_writer('\t<div>\r\n\t\t<a href="/homepage/checkout/')
            __M_writer(str( user.id ))
            __M_writer('" class="btn btn-warning text-right">Checkout</a>\r\n\t</div>\r\n')
        else:
            __M_writer('\t<h3>Your shopping cart is empty! Take a look at some of our products and find a little something that you like.</h3>\r\n\t<a href="/homepage/catalog/" class="btn btn-primary">Go to Catalog</a>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/shoppingcart.html", "uri": "shoppingcart.html", "line_map": {"64": 7, "65": 8, "66": 10, "67": 11, "68": 13, "69": 13, "70": 14, "71": 14, "72": 18, "73": 18, "74": 22, "75": 23, "76": 25, "77": 26, "78": 26, "16": 2, "82": 28, "83": 31, "84": 31, "85": 34, "86": 34, "87": 38, "88": 39, "89": 40, "90": 40, "91": 42, "92": 43, "29": 0, "99": 93, "41": 1, "42": 2, "93": 46, "52": 4, "63": 4}}
__M_END_METADATA
"""
