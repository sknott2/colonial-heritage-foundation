from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import homepage.models as hmod
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
from django.contrib.auth.hashers import make_password

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {}

	return templater.render_to_response(request, 'login.html', params)

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	def clean(self):
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		if user == None:
			s = Server('www.colonialheritagefoundation.co', port=3890, get_info=GET_ALL_INFO)
			c = Connection(
				s,
				auto_bind = True,
				user = self.cleaned_data['username']+'@colonialheritagefoundation.local',
				password= self.cleaned_data['password'],
				authentication=AUTH_SIMPLE,
				client_strategy=STRATEGY_SYNC, 
				raise_exceptions=False
			)
			if c.response is None:
				search_results = c.search(
					search_base = 'CN=Users,DC=colonialheritagefoundation,DC=local',
					search_filter = '(samAccountName=Dennis)',
					attributes = [
						'givenName',
						'sn',
						'mail',]
				)
				user = hmod.User()
				address = hmod.Address()
				address.zip = 0
				address.save()
				user.username = self.cleaned_data['username']
				user.password = make_password(self.cleaned_data['password'])
				user.first_name = c.response[0]['attributes']['givenName']
				user.last_name = c.response[0]['attributes']['sn']
				user.email = self.cleaned_data['username']+'@colonialheritagefoundation.co'
				user.address = address
				user.save()
			else:
				raise forms.ValidationError('Your username and password do not match.')
		return self.cleaned_data

@view_function
def loginform(request):
	params = {}

	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data['username'])
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			user_object = hmod.User.objects.get(username=form.cleaned_data['username'])
			return HttpResponseRedirect('/homepage/accounts/{}/'.format(user_object.id))
	params['form'] = form
	return templater.render_to_response(request, 'login.loginform.html', params)

@view_function
def log_out(request):
	logout(request)
	return templater.render_to_response(request, 'logout.html')
