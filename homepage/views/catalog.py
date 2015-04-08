from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function
#from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from homepage import models as hmod
import re
from django.db.models import Q

templater = get_renderer('homepage')

@view_function
def process_request(request):

	params = {}
	query_string = ''

	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['name','description'])
		params['products'] = hmod.Product.objects.filter(entry_query).order_by('name')
		params['items'] = hmod.Item.objects.filter(entry_query).order_by('name')
	else: 
		params['products'] = hmod.Product.objects.all().order_by('name')
		params['items'] = hmod.Item.objects.all().order_by('name')
	params['query_string'] = query_string
	return templater.render_to_response(request,'/catalog.html', params)


def normalize_query(query_string,
					findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
					normspace=re.compile(r'\s{2,}').sub):
	''' Splits the query string in invidual keywords, getting rid of unecessary spaces
		and grouping quoted words together.
		Example:
		
		>>> normalize_query('  some random  words "with   quotes  " and   spaces')
		['some', 'random', 'words', 'with quotes', 'and', 'spaces']
	
	'''
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
	''' Returns a query, that is a combination of Q objects. That combination
		aims to search keywords within a model by testing the given search fields.
	
	'''
	query = None # Query to search for every search term        
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None # Query to search for a given term in each field
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query
	#catalog_items = hmod.Product.objects.all()
	
	#template_vars['catalog_items'] = catalog_items
	return templater.render_to_response(request, 'catalog.html', template_vars)

@view_function
def detail(request):
	template_vars = {}

	product = hmod.Product.objects.get(id=request.urlparams[0])
	template_vars['product'] = product
	return templater.render_to_response(request, 'catalog.detail.html', template_vars)

class QuantityForm(forms.Form):
	quantity = forms.IntegerField(min_value=0, max_value=50)

	def clean_quantity(self):
		if self.cleaned_data['quantity'] > 50:
			raise forms.ValidationError('We only allow orders of maximum 50 units at a time')
		if self.cleaned_data['quantity'] < 1:
			raise forms.ValidationError('Please enter a positive number')
		return self.cleaned_data['quantity']

@view_function
def item_detail(request):
	params = {}

	item = hmod.Item.objects.get(id=request.urlparams[0])
	params['item'] = item

	return templater.render_to_response(request, 'catalog.detail.item.html', params) 