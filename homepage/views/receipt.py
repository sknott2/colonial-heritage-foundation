from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
#rom .. import dmp_render, dmp_render_to_response
from django.shortcuts import render
import homepage.models as hmod
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
import datetime


templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {}

	todays_date = datetime.datetime.now()
	customer = hmod.User.objects.get(id=request.urlparams[0])
	order = hmod.Order.objects.get(id=request.urlparams[1])
	print(order.id)
	print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
	total = request.urlparams[2]
	items = []
	products = []
	try:
		opo = hmod.OnlinePurchaseOrder.objects.get(order_id=order.id)
		print()
		opp = hmod.OnlinePurchaseProduct.objects.filter(onlinepurchaseorder_id=opo.id)
		for product in opp:
			product_obj = hmod.Product.objects.get(id=product.product_id)
			print('###################################################################################################################')
			print(product_obj.name)
			products.append(product_obj)
		template_vars['opo'] = opo
		#params['products'] = opp
	except:
		pass
	print('#####################################################################################################################')
	print(products)
	#rental=hmod.Rental.objects.get(order=order.id)
	#print(rental.order_id)
	print('**********************************')
	try:
		rental = hmod.Rental.objects.get(order=order.id)
		print(rental.order_id)
		rentalitem = hmod.RentalItem.objects.filter(rental_id_id=rental.id)
		for item in rentalitem:
			item_obj = hmod.Item.objects.get(id=item.item_id_id)
			print(item_obj)
			items.append(item_obj)
		print(items)
		template_vars['rental'] = rental
		#params['items'] = items
	except:
		pass
	print('#####################################################################################################################')
	print(items)

	subject = "Confirmation of order from Colonial Heritage Foundation"
	from_email = settings.EMAIL_HOST_USER
	to_list = [ customer.email ]
	print(products)
	template_vars = {
		'customer':customer,
		'total':total,
		'products':products,
		'items':items,
		'order':order,
	}
	print(items)
	print(products)
	message = templater.render(request, 'receipt_email_template.html', template_vars)
	send_mail(subject, message, from_email, to_list, html_message=message, fail_silently=False)

	print(">>>>>>>>>>>>>>>>>>>>>>>> sending email.....")

	print(products)
	return templater.render_to_response(request, 'receipt.html', template_vars)
