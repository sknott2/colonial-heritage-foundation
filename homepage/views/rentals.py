from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django import forms
import homepage.models as hmod
import time
from datetime import datetime
from datetime import timedelta
from datetime import date
import datetime
import smtplib
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail

templater = get_renderer('homepage')

@view_function
@permission_required('homepage.change_rental', login_url='/homepage/index')
def process_request(request):
	params = {}

	rentals = hmod.Rental.objects.all()
	params['rentals'] = rentals

	return templater.render_to_response(request, 'rentals.html', params)

@view_function
@permission_required('homepage.change_rental', login_url='/homepage/index')
def edit(request):
	params = {}

	try:
		rental = hmod.Rental.objects.get(id=request.urlparams[0])
	except hmod.Rental.DoesNotExist:
		return HttpResponseRedirect('/homepage/rentals/')

	form = RentalEditForm(initial={
		'rental_time' : rental.rental_time,
		'due_date' : rental.due_date,
		'discount_percent' : rental.discount_percent,
	})
	if request.method == 'POST':
		form = RentalEditForm(request.POST)
		if form.is_valid():
			rental.rental_time = form.cleaned_data['rental_time']
			rental.due_date = form.cleaned_data['due_date']
			rental.discount_percent = form.cleaned_data['discount_percent']
			rental.save()
			return HttpResponseRedirect('/homepage/rentals/')

	params['rental'] = rental
	params['form'] = form
	return templater.render_to_response(request, 'rentals.edit.html', params)

class RentalEditForm(forms.Form):
	rental_time = forms.CharField(required=True, min_length=1, max_length=100)
	due_date = forms.CharField(required=True, min_length=1, max_length=100)
	discount_percent = forms.DecimalField(required=True, max_digits=10, decimal_places=2)

	def clean_discount_percent(self):
		if self.cleaned_data['discount_percent'] < 0:
			raise forms.ValidationError('Please enter a positive value')
		if self.cleaned_data['discount_percent'] > 100:
			raise forms.ValidationError('Please enter a valid value (less than 100)')
		return self.cleaned_data['discount_percent']

@view_function
@permission_required('homepage.add_rental', login_url='/homepage/index')
def create(request):
	rental = hmod.Rental()
	rental.rental_time = '2000-01-01 00:00:01'
	rental.due_date = '2000-01-01 00:00:01'
	rental.discount_percent = 0.00
	rental.save()

	return HttpResponseRedirect('/homepage/rentals.edit/{}/'.format(rental.id))

@view_function
@permission_required('homepage.delete_rental', login_url='/homepage/index')
def delete(request):
	
	try:
		rental = hmod.Rental.objects.get(id=request.urlparams[0])
	except hmod.Rental.DoesNotExist:
		return HttpResponseRedirect('/homepage/rentals/')

	rental.delete()

	return HttpResponseRedirect('/homepage/rentals/')


@view_function
def return_users(request):
	params = {}

	form = ReturnUser()
	if request.method == 'POST':
		form = ReturnUser(request.POST)
		if form.is_valid():
			#get the user and agent who are returning an item
			try:
				user = hmod.User.objects.get(username=form.cleaned_data['Username'])
				agent = hmod.Agent.objects.get(username=form.cleaned_data['Agent_Username'])
			except hmod.User.DoesNotExist:
				return HttpResponseRedirect('/homepage/rentals.return_users/')
			return HttpResponseRedirect('/homepage/rentals.return_item/{}/{}'.format(user.id, agent.id))

	params['form'] = form
	return templater.render_to_response(request, 'rentals.return_users.html', params)

class ReturnUser(forms.Form):
	Username = forms.CharField(required=True, min_length=1, max_length=100)
	Agent_Username = forms.CharField(required=True, min_length=1, max_length=100)

@view_function
def return_item(request):
	params = {}
	user = hmod.User.objects.get(id=request.urlparams[0])
	agent = hmod.Agent.objects.get(id=request.urlparams[1])
	rental_list = []
	#get the orders that the user has made
	orders = hmod.Order.objects.filter(customer=hmod.User.objects.get(id=request.urlparams[0]))
	for order in orders:
		try:
			#get the rental id's associated with those orders
			rental_list.append(hmod.Rental.objects.get(id=order.id))
		except hmod.Rental.DoesNotExist:
			pass

	item_list = []
	for rental in rental_list:
		#get the items that have been rented to the user
		items = hmod.RentalItem.objects.filter(rental_id_id=rental.id)
		for item in items:
			item_list.append(item)

	loaned_list = []
		#check which items have been returned and show only non-returned items
	for item_object in item_list:
		item = hmod.RentalItem.objects.get(id=item_object.id)
		if item.returns == None:
			loaned_list.append(hmod.Item.objects.get(id=item.item_id_id))
		else:
			pass

	params['loaned_list'] = loaned_list
	params['user'] = user
	params['agent'] = agent

	return templater.render_to_response(request, 'rentals.return_item.html', params)

@view_function
def return_rental(request):
	params = {}
	user = hmod.User.objects.get(id=request.urlparams[0])
	agent = hmod.Agent.objects.get(id=request.urlparams[1])

	returned_item = hmod.Item.objects.get(id=request.urlparams[2])
	rental_item = hmod.RentalItem.objects.get(item_id_id=returned_item.id, returns_id=None)
	rental = hmod.Rental.objects.get(id=rental_item.rental_id_id)

	#CREATE NEW INSTANCE OF RETURN
	new_return = hmod.Return()
	new_return.return_time = date.today()
	new_return.agent = agent
	new_return.rental = rental
	new_return.save()

	rental_item.returns = new_return
	rental_item.save()

	#SET UP DATES TO BE COMPARED
	mdate = rental.due_date.date()
	mdate = mdate.strftime("%Y-%m-%d")
	rdate = date.today()
	rdate = rdate.strftime("%Y-%m-%d")
	mdate1 = datetime.datetime.strptime(mdate, "%Y-%m-%d").date()
	rdate1 = datetime.datetime.strptime(rdate, "%Y-%m-%d").date()
	delta = 0

	#IF THE RETURN DATE IS GREATER THAN THE DUE DATE, DO THIS
	if mdate < rdate:
		days_late = date.today() - rental.due_date.date()
		delta = (rdate1-mdate1).days
		fee = delta * (returned_item.standard_rental_price / 7)
		fee = round(fee, 2)
		status = 'Your return was a little late...'

		lf = hmod.LateFee()
		lf.amount = fee
		lf.return_fee = new_return
		lf.rental_item = rental_item
		lf.days_late = delta
		lf.save()

	#IF THE ITEM WAS RETURNED BEFORE THE DUE DATE, DO THIS
	else:
		status = 'You brought it back on time! Thanks!'
		lf = hmod.LateFee.objects.get(id=1)
		print('its not overdue')

	params['status'] = status
	params['delta'] = delta
	params['new_return'] = new_return
	params['user'] = user
	params['rental'] = rental
	params['returned_item'] = returned_item
	params['agent'] = agent
	params['lf'] = lf
	return templater.render_to_response(request, 'rentals.return_rental.html', params)

@view_function
def return_damageFee(request):
	params = {}

	user = hmod.User.objects.get(id=request.urlparams[0])
	agent = hmod.Agent.objects.get(id=request.urlparams[1])
	return_fee = hmod.Return.objects.get(id=request.urlparams[2])
	rental = hmod.Rental.objects.get(id=request.urlparams[3])
	item = hmod.Item.objects.get(id=request.urlparams[4])
	rental_item = hmod.RentalItem.objects.get(rental_id_id=rental.id, item_id_id=item.id)

	form = DamageForm()
	if request.method == 'POST':
		form = DamageForm(request.POST)
		if form.is_valid():
			DmgFee = hmod.DamageFee()
			DmgFee.amount = form.cleaned_data['Fee']
			DmgFee.return_fee = return_fee
			DmgFee.rental_item = rental_item
			DmgFee.description = form.cleaned_data['Description']
			DmgFee.save()
			return HttpResponseRedirect('/homepage/rentals.return_item/{}/{}/'.format(user.id, agent.id))
	params['form'] = form
	params['user'] = user
	params['agent'] = agent
	params['return_fee'] = return_fee
	params['rental'] = rental
	params['item'] = item
	params['rental_item'] = rental_item
	return templater.render_to_response(request, 'rentals.return_damageFee.html', params)
	

class DamageForm(forms.Form):
	Description = forms.CharField(required=True, min_length=1, max_length=1000)
	Fee = forms.DecimalField(required=True, max_digits=10, decimal_places=2)

@view_function
def overdue_rentals(request):
	params = {}
	overdue_list = []

	rental_item = hmod.RentalItem.objects.all()
	for item in rental_item:
		if item.returns == None:
			overdue_list.append(item)
		else:
			pass

	today = date.today()
	thirty = today - datetime.timedelta(days=30)
	sixty = today - datetime.timedelta(days=60)
	ninety = today - datetime.timedelta(days=90)

	latelist = []
	latethirtylist = []
	latesixtylist = []
	lateninetylist = []
	users = {}
	userlist = []

	for obj in overdue_list:
		rental = hmod.Rental.objects.get(id=obj.rental_id_id)
		duedate = rental.due_date.date()

		order = hmod.Order.objects.get(id=rental.order_id)
		item = hmod.Item.objects.get(id=obj.item_id_id)
		user = hmod.User.objects.get(id=order.customer_id)
		users[user.id] = user.username

		userlist.append(user.username)

		if duedate < ninety:
			lateninetylist.append(item)
		elif duedate < sixty:
			latesixtylist.append(item)
		elif duedate < thirty:
			latethirtylist.append(item)
		elif duedate < today:
			latelist.append(item)
		else:
			pass

	params['latelist'] = latelist
	params['latethirtylist'] = latethirtylist
	params['latesixtylist'] = latesixtylist
	params['lateninetylist'] = lateninetylist
	params['userlist'] = userlist
	return templater.render_to_response(request, 'rentals.overdue_rentals.html', params)

@view_function
def email_late(request):
	subject = "Colonial Heritage Foundation : Notice of overdue rental items"

	overdue_list = []

	rental_item = hmod.RentalItem.objects.all()
	for item in rental_item:
		if item.returns == None:
			overdue_list.append(item)
		else:
			pass

	rent_list = []

	for item in overdue_list:
		rent = hmod.Rental.objects.get(id=item.rental_id_id)
		rent_list.append(rent)

	order_list = []

	for item in rent_list:
		order = hmod.Order.objects.get(id=item.order_id)
		order_list.append(order)

	user_list = []

	for item in order_list:
		user = hmod.User.objects.get(id=item.customer_id)
		if user.id not in user_list:
			user_list.append(user.id)
		else:
			pass

	for user_id in user_list:
		user = hmod.User.objects.get(id=user_id)
		all_orders = hmod.Order.objects.filter(customer_id=user.id)

		user_rentals = []
		for order in all_orders:
			rental=hmod.Rental.objects.get(order_id=order.id)
			user_rentals.append(rental)

		user_items = []
		for rental in user_rentals:
			rental_items = hmod.RentalItem.objects.filter(rental_id_id=rental.id)
			for ri in rental_items:
				rental = hmod.Rental.objects.get(id=ri.rental_id_id)
				mdate = rental.due_date.date()
				mdate = mdate.strftime("%Y-%m-%d")
				rdate = date.today()
				rdate = rdate.strftime("%Y-%m-%d")
				if ri.returns == None:
					if mdate <= rdate:
						item = hmod.Item.objects.get(id=ri.item_id_id)
						print(item.name)
						user_items.append(item.name)
					else:
						pass
				else:
					pass

		from_email = settings.EMAIL_HOST_USER
		to_list = [ user.email ]

		template_vars = {
			'user':user.first_name,
			'user_items':user_items,

		}

		message = templater.render(request, 'overdue_emails.html', template_vars)
		send_mail(subject, message, from_email, to_list, html_message=message, fail_silently=False)

	return HttpResponseRedirect('/homepage/rentals.overdue_rentals/')