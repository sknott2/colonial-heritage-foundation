# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428168617.075995
_enable_loop = True
_template_filename = '/Users/Dennis/Developer/Python/chf/homepage/templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n        <div class="row">\n')
        for Event in events:
            __M_writer('            <div class="col-sm-4">\n                <div class="thumbnail product" id="thumbnail">\n                    <div class="item_container text-center">\n                        <img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/events/')
            __M_writer(str( Event.id ))
            __M_writer('.jpg" style="width: 150px; height: 150px;" alt="Image not available"/>\n                        <div class="caption" style="text-align:center;">\n                            <h3 class="name">')
            __M_writer(str( Event.event_name ))
            __M_writer('</h3>\n                            <p class="date"> ')
            __M_writer(str( Event.start_date.strftime('%x') ))
            __M_writer(' to ')
            __M_writer(str( Event.end_date.strftime('%x') ))
            __M_writer('</p>\n\n                            <p>Venue name: ')
            __M_writer(str( Event.venue.name ))
            __M_writer(' </p>\n                            <p>Venue address: ')
            __M_writer(str( Event.venue.address.address_1 ))
            __M_writer(', ')
            __M_writer(str( Event.venue.address.city ))
            __M_writer(' ')
            __M_writer(str( Event.venue.address.state ))
            __M_writer(' </p>\n                            <p><a href="/homepage/areas/')
            __M_writer(str( Event.id ))
            __M_writer('" class="btn btn-sm btn-info">View Areas</a>\n                        </div>\n                    </div>\n                </div>\n            </div>\n')
        __M_writer('        </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 14, "65": 14, "66": 14, "67": 16, "68": 16, "69": 17, "70": 17, "71": 17, "72": 17, "73": 17, "74": 17, "75": 18, "76": 18, "77": 24, "83": 77, "27": 0, "36": 1, "46": 3, "54": 3, "55": 7, "56": 8, "57": 11, "58": 11, "59": 11, "60": 11, "61": 13, "62": 13, "63": 14}, "source_encoding": "ascii", "filename": "/Users/Dennis/Developer/Python/chf/homepage/templates/events.html", "uri": "events.html"}
__M_END_METADATA
"""
