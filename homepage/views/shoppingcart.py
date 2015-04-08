from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
#from .. import dmp_render, dmp_render_to_response
from homepage import models as hmod
templater = get_renderer('homepage')
@view_function
def process_request(request):
	template_vars = {}
	
	cart_products = []
	cart_items = request.session.get('shopping_cart')

	try:
		cart_product_size = len(cart_items)
	except:
		cart_product_size = 0

	if cart_product_size > 0:
		for product in cart_items:
			qty = request.session['shopping_cart'][product]
			citem = hmod.Product.objects.get(id=product)

			cart_products.append([citem, qty])
	else:
		pass

	cart_items = []
	cart_items_rentals = request.session.get('shopping_cart_items')

	try:
		cart_item_size = len(cart_items_rentals)
	except:
		cart_item_size = 0
		
	print(cart_item_size)
	
	if cart_item_size > 0:
		for item in cart_items_rentals:
			qty = request.session['shopping_cart_items'][item]
			citem = hmod.Item.objects.get(id=item)

			cart_items.append([citem, qty])
	
	template_vars['cart_items'] = cart_items
	template_vars['cart_products'] = cart_products
	template_vars['cart_item_size'] = cart_item_size
	template_vars['cart_product_size'] = cart_product_size
	return templater.render_to_response(request, 'shoppingcart.html', template_vars)
	

@view_function
def add(request):
	params = {}
	if request.method == "POST":
		template_vars = {}
		if 'shopping_cart' not in request.session:
			request.session['shopping_cart'] = {}
		pid = request.urlparams[0]
		qty = int(request.POST.get('quantity'))

		if pid in request.session['shopping_cart']:
			request.session['shopping_cart'][pid] += int(qty)
		else:
			request.session['shopping_cart'][pid] = int(qty)
		request.session.modified = True
		return HttpResponseRedirect('/homepage/shoppingcart/')
	else:
		print("SHOW QUANTITY FORM")
		form = QuantityForm()

	user = request.user
	params['user'] = user
	params['form'] = form
	return templater.render_to_response(request, 'quantity.html', params)

class QuantityForm(forms.Form):
	quantity = forms.IntegerField(min_value=0, max_value=50)

	def clean_quantity(self):
		if self.cleaned_data['quantity'] > 50:
			raise forms.ValidationError('We only allow orders of maximum 50 units at a time')
		if self.cleaned_data['quantity'] < 1:
			raise forms.ValidationError('Please enter a positive number')
		return self.cleaned_data['quantity']

@view_function
def delete(request):
	template_vars = {}

	pid = request.urlparams[0]
	qty = request.urlparams[1]

	del request.session['shopping_cart'][pid]
	request.session.modified = True
	
	return HttpResponseRedirect('/homepage/catalog/')
	#del request.session['fav_color']'''

@view_function
def delete_item(request):
	template_vars = {}

	pid = request.urlparams[0]
	#qty = request.urlparams[1]

	del request.session['shopping_cart_items'][pid]
	request.session.modified = True
	
	return HttpResponseRedirect('/homepage/catalog/')
	#del request.session['fav_color']'''

@view_function
def add_item(request):
	params = {}
	template_vars = {}
	if 'shopping_cart_items' not in request.session:
		request.session['shopping_cart_items'] = {}
	pid = request.urlparams[0]
	qty = 1
	if pid in request.session['shopping_cart_items']:
		pass
	else:
		request.session['shopping_cart_items'][pid] = int(qty)
	request.session.modified = True
	return HttpResponseRedirect('/homepage/shoppingcart/')
