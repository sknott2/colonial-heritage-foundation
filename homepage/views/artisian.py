from django.conf import settings
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django_mako_plus.controller.router import get_renderer
from django.http import HttpRequest
import random
from django.contrib.auth.decorators import permission_required
from django.shortcuts  import render_to_response,redirect
import re
from django.db.models import Q


templater = get_renderer('homepage')


#### Shows the lists of events
@view_function
def process_request(request):
    params = {}

    try:
        area_id = hmod.Area.objects.get(id=request.urlparams[0])
    except hmod.Area.DoesNotExist:
        return HttpResponseRedirect('/homepage/events/')

    params['area_id'] = area_id
    params['areaproducts'] = hmod.AreaProduct.objects.filter(area_id=area_id)

    return templater.render_to_response(request, 'artisian.html', params)