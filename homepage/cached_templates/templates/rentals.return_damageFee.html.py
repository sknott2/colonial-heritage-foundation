# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428113708.99166
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/rentals.return_damageFee.html'
_template_uri = 'rentals.return_damageFee.html'
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        return_fee = context.get('return_fee', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        agent = context.get('agent', UNDEFINED)
        item = context.get('item', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        return_fee = context.get('return_fee', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        agent = context.get('agent', UNDEFINED)
        item = context.get('item', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div>\r\n\t\tWhat damages are there?\r\n\t\t<form method="POST" action=\'/homepage/rentals.return_damageFee/')
        __M_writer(str( user.id ))
        __M_writer('/')
        __M_writer(str( agent.id ))
        __M_writer('/')
        __M_writer(str( return_fee.id ))
        __M_writer('/')
        __M_writer(str( rental.id ))
        __M_writer('/')
        __M_writer(str( item.id ))
        __M_writer("/'>\r\n\t\t\t")
        __M_writer(str( form.as_p() ))
        __M_writer('\r\n\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t</form>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/rentals.return_damageFee.html", "source_encoding": "ascii", "uri": "rentals.return_damageFee.html", "line_map": {"64": 6, "65": 6, "66": 6, "67": 6, "68": 6, "69": 6, "70": 6, "71": 6, "40": 1, "73": 7, "74": 7, "80": 74, "72": 6, "50": 3, "27": 0, "62": 3, "63": 6}}
__M_END_METADATA
"""
