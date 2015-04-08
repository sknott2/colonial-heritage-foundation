from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
#from .. import dmp_render, dmp_render_to_response
from django.shortcuts import render
import homepage.models as hmod
from django.contrib.auth.decorators import permission_required
from time import gmtime, strftime
from datetime import datetime, timedelta
import requests

templater = get_renderer('homepage')


@view_function
def process_request(request):
	template_vars = {}
	current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	user = request.user#hmod.User.objects.get(id=request.urlparams[0])
	form = OrderForm()
	prod_cart_objects = []
	item_cart_objects = []

	cart_products = request.session.get('shopping_cart')

	rent_total = 0
	pur_total = 0

	if not cart_products: 
		pass
	else:
		for product in cart_products:
			qty = request.session['shopping_cart'][product]
			citem = hmod.Product.objects.get(id=product)
			print(citem)
			prod_cart_objects.append([citem.id, qty])
		for item in prod_cart_objects:
			citem = hmod.Product.objects.get(id=item[0])
			quant = item[1]
			pur_total = pur_total + (citem.current_price * quant)


	cart_items = request.session.get('shopping_cart_items')
	if not cart_items:
		pass
	else:
		for item in cart_items:
			qty = request.session['shopping_cart_items'][item]
			citem = hmod.Item.objects.get(id=item)
			print(citem)
			item_cart_objects.append([citem.id, qty])

		for item in item_cart_objects:
			citem = hmod.Item.objects.get(id=item[0])
			rent_total = rent_total + citem.standard_rental_price

	total = rent_total + pur_total

	print(prod_cart_objects)
	print(item_cart_objects)

	prod_cart_size = len(prod_cart_objects)
	item_cart_size = len(item_cart_objects)

	print(prod_cart_size)
	print(item_cart_size)

	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			print('Form data cleaned')
			print('Charge ID: '+form.cleaned_data['charge'])

			address = hmod.Address()
			address.address_1=form.cleaned_data['address_1']
			address.address_2=form.cleaned_data['address_2']
			address.city=form.cleaned_data['city']
			address.state=form.cleaned_data['state']
			address.zip=form.cleaned_data['zip']
			address.save()
			
			pur_total = 0
			rent_total = 0
			new_opo_id = 0
			new_rent_id = 0

			if not prod_cart_objects:
				pass
			else:

				opo = hmod.OnlinePurchaseOrder()
				opo.save()
				new_opo_id = opo.id
				for item in prod_cart_objects:
					citem = hmod.Product.objects.get(id=item[0])
					quant = item[1]
					pur_total = pur_total + (citem.current_price * quant)

					opp = hmod.OnlinePurchaseProduct()
					opp.product_id = citem.id
					opp.onlinepurchaseorder=hmod.OnlinePurchaseOrder(id=opo.id)
					opp.quantity = quant
					opp.save()
				opo.total=pur_total
				opo.save()

				print('########################################################################')
			if not item_cart_objects:
				pass
			else:
				rental = hmod.Rental()
				rental.rental_time = current_time
				mytime = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
				mytime += timedelta(hours=6)
				due_date = mytime.strftime("%Y-%m-%d %H:%M:%S")
				rental.due_date = due_date
				rental.save()
				print('1111111111111111111111111111111111111111111111111111111111111')
				new_rent_id = rental.id
				for item in item_cart_objects:
					citem = hmod.Item.objects.get(id=item[0])
					rent_total = rent_total + citem.standard_rental_price
					
					rentitem = hmod.RentalItem()
					rentitem.item_id_id = citem.id
					rentitem.rental_id_id = rental.id
					rentitem.returns = None
					rentitem.save()
				rental.total = rent_total
				rental.save()
				print('########################################################################')

			total = rent_total + pur_total
			#print(customer)
			print('1111111111111111111111111111111111111111111111111111111111111')
			order = hmod.Order()
			print('1')
			order.customer = hmod.User.objects.get(id=user.id)
			print('2')
			order.ships_to = hmod.Address.objects.get(id=address.id)
			print('3')
			#order.payment = form.cleaned_data['charge']
			print('4')
			order.order_date = current_time
			print('5')
			order.save()
			if new_opo_id != 0:
				new_opo = hmod.OnlinePurchaseOrder.objects.get(id=new_opo_id)
				new_opo.order = order
				new_opo.save()
			if new_rent_id != 0:
				new_rental = hmod.Rental.objects.get(id=new_rent_id)
				new_rental.order = order
				new_rental.save()

			url = '/homepage/receipt/' + str(user.id) + '/' + str(order.id) + '/' + str(total) + '/'

			try:
				del request.session['shopping_cart']
			except:
				pass

			try:
				del request.session['shopping_cart_items']
			except:
				pass

			return HttpResponseRedirect(url)
	form = OrderForm(initial={
		'total': total,
		'Card_Holder_Name': user.first_name+' '+user.last_name,
	})
	template_vars['form'] = form
	template_vars['total'] = total
	return templater.render_to_response(request, 'checkout.html', template_vars)

class OrderForm(forms.Form):
	Card_Holder_Name = forms.CharField()
	credit_number = forms.CharField()
	card_type = forms.CharField()
	security_code = forms.IntegerField()
	expiration_date = forms.DateField()
	address_1 = forms.CharField()
	address_2 = forms.CharField(required=False)
	city = forms.CharField()
	state = forms.CharField()
	zip = forms.IntegerField()
	total = forms.CharField(widget=forms.HiddenInput)

	def clean(self):
		# send the request with the data
		API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
		API_KEY = 'c0b428a37a6b9820e532bd345fe3b997'

		r = requests.post(API_URL, data={
		  'apiKey': API_KEY,
		  'currency': 'usd',
		  'amount': self.cleaned_data['total'],
		  'type': self.cleaned_data['card_type'],
		  'number': self.cleaned_data['credit_number'],
		  'exp_month': '10',
		  'exp_year': '15',
		  'cvc': self.cleaned_data['security_code'],
		  'name': self.cleaned_data['Card_Holder_Name'],
		  'description': 'Charge for '+self.cleaned_data['Card_Holder_Name'],
		})

		print('----------------------------------------')
		print('Posting API call!')
		# just for debugging, print the response text
		print(r.text)

		# parse the response to a dictionary
		resp = r.json()
		if 'error' in resp:
			print("ERROR: ", resp['error'])
			raise forms.ValidationError('There was an error processing your card: '+resp['error'])
		else:
			self.cleaned_data['charge'] = resp['ID']
		return self.cleaned_data