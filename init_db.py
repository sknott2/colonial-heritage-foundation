
#!/usr/bin/env python3

#initialize django
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'chf.settings'
import django
django.setup()

#regular imports
import random, re
from django import forms
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

##### DROP DATABASE, RECREATE IT, THEN MIGRATE IT #################

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])
'''
##### CREATE PERMISSIONS/GROUPS #####################
Group.objects.all().delete()

group = Group()
group.name = "Admin"
group.save()
group.permissions.add(permission)

group = Group()
group.name = "Manager"
group.save()
group.permissions.add(permission)

group = Group()
group.name = "User"
group.save()
group.permissions.add(permission)

'''

#Create Addresses
#Address_1, Address_2, City, State, ZIP
for data in [
	['1234 Colonial Dr.', '', 'Provo', 'UT', 84606],
	['7894 Eagle Dr.', '', 'Provo', 'UT', 84606],
	['4512 State St.', '', 'Provo', 'UT', 84604],
	['1478 Retail Dr.', '', 'Provo', 'UT', 84606],
	['148 Agent Dr.', '', 'Provo', 'UT', 84606],
	['1234 Venue St.', '', 'Provo', 'UT', 84604],
]:
	address = hmod.Address()
	address.address_1 = data[0]
	address.address_2 = data[1]
	address.city = data[2]
	address.state = data[3]
	address.zip = data[4]
	address.save()

#Create Photographs
#date_taken, place_taken, image, caption
for data in [
	['2014-11-12', '', 'SockPhotoPath', 'A picture of some socks'],
	['2014-08-23', 'Event', 'EventPhotoPath', 'A picture of Event Location'],
]:
	photo = hmod.Photograph()
	photo.date_taken = data[0]
	photo.place_taken = data[1]
	photo.image = data[2]
	photo.caption = data[3]
	photo.save()

#Create Organizations
#name, organization_type, address_id
for data in [
	['Walmart', 'Retail', hmod.Address.objects.get(address_1='1478 Retail Dr.')],
	['Target', 'Retail', hmod.Address.objects.get(address_1='1478 Retail Dr.')]
]:
	organization = hmod.Organization()
	organization.name = data[0]
	organization.organization_type = data[1]
	organization.address = data[2]
	organization.save()

#Create Users
#password, is_superuser, username, first_name, last_name, email, is_staff, birth_date, address_id, organization_id
for data in [
	['password', True, 'SuperUser', 'Robert', 'Hoeft', 'RobertHoeft1991@gmail.com', True, '1991-12-27', hmod.Address.objects.get(id=1), None],
	['password', False, 'AdminUser', 'Devin', 'Adams', 'robhoeft@outlook.com', False, '1991-12-09', hmod.Address.objects.get(id=2), 1]#,
]:
	user = hmod.User()
	user.set_password(data[0])
	user.is_superuser = data[1]
	user.username = data[2]
	user.first_name = data[3]
	user.last_name = data[4]
	user.email = data[5]
	user.is_staff = data[6]
	user.birth_date = data[7]
	user.address = data[8]
	user.organization_id = data[9]
	user.save()
'''
#Create Payment instances
#credit card number, card type, security code, expiration_date
for data in [
	[2584784875635124, 'Visa', 123, '2015-12-01', hmod.Address.objects.get(id=1), hmod.User.objects.get(id=1)],
	[5461257894512345, 'Mastercard', 657, '2015-11-01', hmod.Address.objects.get(id=1), hmod.User.objects.get(id=1)],
	[5123487954365125, 'Visa', 183, '2016-01-01', hmod.Address.objects.get(id=1), hmod.User.objects.get(id=1)],
]:
	payment = hmod.Payment()
	payment.credit_number = data[0]
	payment.card_type = data[1]
	payment.security_code = data[2]
	payment.expiration_date = data[3]
	payment.bills_to = data[4]
	payment.customer = data[5]
	payment.save()
'''
#Create Agents
#password, is_superuser, username, first_name, last_name, email, is_staff, birth_date, address_id, organization_id, appointment date
for data in [
	['password', False, 'Agent', 'Sarah', 'Knott', 'robhoeft@outlook.com', True, '1993-06-16', hmod.Address.objects.get(id=5), None, '2014-12-15']
]:
	agent = hmod.Agent()
	agent.set_password(data[0])
	agent.is_superuser = data[1]
	agent.username = data[2]
	agent.first_name = data[3]
	agent.last_name = data[4]
	agent.email = data[5]
	agent.is_staff = data[6]
	agent.birth_date = data[7]
	agent.address = data[8]
	agent.organization_id = data[9]
	agent.appointment_date = data[10]
	agent.save()

#Create Venue
#Venue name, photo of venue, address of venue
for data in [
	['Chatfield Park', hmod.Photograph.objects.get(id=1), hmod.Address.objects.get(id=6)],
	['Pinkerton Park', hmod.Photograph.objects.get(id=1), hmod.Address.objects.get(id=2)]
]:
	venue = hmod.Venue()
	venue.name = data[0]
	venue.photo = data[1]
	venue.address = data[2]
	venue.save()

#Create Event
#name, start day, end day, map file, public?, venue
for data in [
	['Colonial Days', '2015-01-10', '2015-01-15', 'map.html', True, hmod.Venue.objects.get(name='Chatfield Park')],
	['Festival of the Past', '2015-04-15', '2015-04-20', 'map.html', True, hmod.Venue.objects.get(id=2)]
]:
	event = hmod.Event()
	event.event_name = data[0]
	event.start_date = data[1]
	event.end_date = data[2]
	event.map_file_name = data[3]
	event.public_event = data[4]
	event.venue = data[5]
	event.save()

#Create Area
for data in [
	['Area1', 'The first area', 1, hmod.Agent.objects.get(id=3), hmod.Agent.objects.get(id=3), hmod.Event.objects.get(id=1)],
	['Area2', 'The second area', 2, hmod.Agent.objects.get(id=3), hmod.Agent.objects.get(id=3), hmod.Event.objects.get(id=1)],
	['Area3', 'The third area', 3, hmod.Agent.objects.get(id=3), hmod.Agent.objects.get(id=3), hmod.Event.objects.get(id=2)]
]:
	area = hmod.Area()
	area.name = data[0]
	area.description = data[1]
	area.place_number = data[2]
	area.coordinator = data[3]
	area.supervisor = data[4]
	area.event = data[5]
	area.save()

#Create Area products
for data in [
	['Shoe Shine', 'Black Shoe Shine', 2.5, 5.5, hmod.Area.objects.get(id=1)],
	['Goose Feathers', 'Stuffing for pillows', 10, 12, hmod.Area.objects.get(id=2)],
	['Shoes', 'Pilgrim Shoes', 22, 30, hmod.Area.objects.get(id=1)],
	['Tent', 'buy a colonial tent here', 17.99, 21.99, hmod.Area.objects.get(id=1)],
	['Butter Churner', 'Churn butter like an olden day pro', 20.99, 22.99, hmod.Area.objects.get(id=2)]
]:
	ap = hmod.AreaProduct()
	ap.name = data[0]
	ap.description = data[1]
	ap.low_price = data[2]
	ap.high_price = data[3]
	ap.area = data[4]
	ap.save()

#Create Participant
for data in [
	['password', False, 'Participant1', 'Derrik', 'Adams', 'robhoeft@outlook.com', False, '1991-12-16', hmod.Address.objects.get(id=1), None, 'I am a twin', 'Brother', 'Devin Adams', '4561234561', hmod.Photograph.objects.get(id=1) ]
]:
	participant = hmod.Participant()
	participant.set_password(data[0])
	participant.is_superuser = data[1]
	participant.username = data[2]
	participant.first_name = data[3]
	participant.last_name = data[4]
	participant.email = data[5]
	participant.is_staff = data[6]
	participant.birth_date = data[7]
	participant.address = data[8]
	participant.organization_id = data[9]
	participant.biographical_sketch = data[10]
	participant.contact_relationship = data[11]
	participant.e_contact_name = data[12]
	participant.e_contact_phone = data[13]
	participant.photo = data[14]
	participant.save()


#Create Role
for data in [
	['Benjamin Franklin', 'Historical Figure', hmod.Participant.objects.get(id=4), hmod.Area.objects.get(id=1)],
	['James Madison', 'Historical Figure', hmod.Participant.objects.get(id=4), hmod.Area.objects.get(id=2)]
]:
	role = hmod.Role()
	role.name = data[0]
	role.type = data [1]
	role.participant = data[2]
	role.area = data[3]
	role.save()

#Create Item
for data in [
	['Gun', 'An old gun', 1500.00, 40, True, hmod.User.objects.get(id=1), hmod.Photograph.objects.get(id=1)],
	['Walking Stick', 'Hickory walking stick', 150.00, 5, False, hmod.User.objects.get(id=1), hmod.Photograph.objects.get(id=1)],
	['Rifle', 'Colonial Hunting Rifle', 1000.00, 35, True, hmod.User.objects.get(id=1), hmod.Photograph.objects.get(id=1)],
	['Bicycle', 'Colonial bike', 1000.00, 35, True, hmod.User.objects.get(id=1), hmod.Photograph.objects.get(id=1)],
	['Whip', 'Colonial whip', 10.00, 3, True, hmod.User.objects.get(id=1), hmod.Photograph.objects.get(id=1)]
]:
	item = hmod.Item()
	item.name = data[0]
	item.description = data[1]
	item.value = data[2]
	item.standard_rental_price = data[3]
	item.is_rentable = data[4]
	item.user = data[5]
	item.photo = data[6]
	item.save()


#Create Wardobe_Item
for data in [
	['Dolly Madison Dress','Dress for actress role Dolly Madison', 50.99, 15.99, False, hmod.User.objects.get(id=1), hmod.Photograph.objects.get(id=1),'M', '33" waist', 'Female','Red','Striped','1799','1805','First lady gown']
]:

	ward = hmod.Wardrobe_Item()
	ward.name = data[0]
	ward.description = data[1]
	ward.value = data[2]
	ward.standard_rental_price = data[3]
	ward.is_rentable = data[4]
	ward.user = data[5]
	ward.photo = data[6]
	ward.size = data[7]
	ward.size_modifier = data[8]
	ward.gender = data[9]
	ward.color = data[10]
	ward.pattern = data[11]
	ward.start_year = data[12]
	ward.end_year = data[13]
	ward.note = data[14]
	ward.save()

#Create Order
for data in [
	[
		'2015-01-15', 
		7202104757, 
		'2015-01-16', 
		'2015-01-15',
		'2015-01-16', 
		1254635, 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.User.objects.get(id=1), 
		hmod.Address.objects.get(id=1),
		'ch_1234m945d153',
		True, 
		True
	],
	[
		'2015-01-22', 
		7202120147, 
		'2015-01-23', 
		'2015-01-23',
		'2015-01-23', 
		1288885, 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.User.objects.get(id=1), 
		hmod.Address.objects.get(id=1),
		'ch_1s5dgg7864dsa',
		True, 
		True
	],
	[
		'2015-01-25', 
		7202120147, 
		'2015-01-27', 
		'2015-01-27',
		'2015-01-27', 
		1288885, 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.User.objects.get(id=1), 
		hmod.Address.objects.get(id=1),
		'ch_546agd5y5h4j',
		True, 
		True
	],
	[
		'2015-01-25', 
		7202120147, 
		'2015-01-27', 
		'2015-01-27',
		'2015-01-27', 
		1288885, 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.User.objects.get(id=1), 
		hmod.Address.objects.get(id=1),
		'ch_78945edgadg',
		True, 
		True
	],
	[
		'2015-01-25', 
		7202120147, 
		'2015-01-27', 
		'2015-01-27',
		'2015-01-27', 
		1288885, 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.Agent.objects.get(id=3), 
		hmod.User.objects.get(id=1), 
		hmod.Address.objects.get(id=1),
		'ch_45612487561',
		True, 
		True
	]
]:
	order = hmod.Order()
	order.order_date = data[0]
	order.phone = data[1]
	order.date_packed = data[2]
	order.date_paid = data[3]
	order.date_shipped = data[4]
	order.tracking_number = data[5]
	order.packed_by = data[6]
	order.shipped_by = data[7]
	order.processed_by = data[8]
	order.customer = data[9]
	order.ships_to = data[10]
	order.payment = data[11]
	order.online_order = data[12]
	order.in_person_pickup = data[13]
	order.save()

#Create Rental
for data in [
	['2015-03-04 12:00:00', '2015-03-15 12:00:00', 5.00, 20, hmod.Order.objects.get(id=2)],
	['2015-03-12 12:00:00', '2015-03-22 12:00:00', 2.00, 15, hmod.Order.objects.get(id=1)],
	['2015-03-25 12:00:00', '2015-04-22 12:00:00', 2.00, 15, hmod.Order.objects.get(id=3)],
	['2015-01-25 12:00:00', '2015-01-27 12:00:00', 2.00, 15, hmod.Order.objects.get(id=4)],
	['2014-12-25 12:00:00', '2014-12-27 12:00:00', 2.00, 15, hmod.Order.objects.get(id=5)]
]:
	rental = hmod.Rental()
	rental.rental_time = data[0]
	rental.due_date = data[1]
	rental.discount_percent = data[2]
	rental.total = data[3]
	rental.order = data[4]
	rental.save()

#Create Return
for data in [
	['2015-03-15 12:00:00', True, hmod.Agent.objects.get(id=3), hmod.Rental.objects.get(id=1)]
]:
	returns = hmod.Return()
	returns.return_time = data[0]
	returns.fees_paid = data[1]
	returns.agent = data[2]
	#returns.payment = data[3]
	returns.rental = data[3]
	returns.save()

#Create RentalItem
for data in [
	[hmod.Rental.objects.get(id=1), hmod.Item.objects.get(id=1), hmod.Return.objects.get(id=1)],
	[hmod.Rental.objects.get(id=1), hmod.Item.objects.get(id=2), hmod.Return.objects.get(id=1)],
	[hmod.Rental.objects.get(id=1), hmod.Item.objects.get(id=3), hmod.Return.objects.get(id=1)],
	[hmod.Rental.objects.get(id=2), hmod.Item.objects.get(id=1), None],
	[hmod.Rental.objects.get(id=2), hmod.Item.objects.get(id=2), None],
	[hmod.Rental.objects.get(id=2), hmod.Item.objects.get(id=3), None],
	[hmod.Rental.objects.get(id=3), hmod.Item.objects.get(id=4), None],
	[hmod.Rental.objects.get(id=4), hmod.Item.objects.get(id=5), None],
	[hmod.Rental.objects.get(id=5), hmod.Item.objects.get(id=6), None]
]:
	ritem = hmod.RentalItem()
	ritem.rental_id=data[0]
	ritem.item_id = data[1]
	ritem.returns = data[2]
	ritem.save()

#Create Late Fee
for data in [
	[0, None, None, 0],
	[26.50, hmod.Return.objects.get(id=1), hmod.RentalItem.objects.get(id=1), 4],
	[13.00, hmod.Return.objects.get(id=1), hmod.RentalItem.objects.get(id=2), 1],
	[5.00, hmod.Return.objects.get(id=1), hmod.RentalItem.objects.get(id=3), 1]
]:
	latefee = hmod.LateFee()
	latefee.amount = data[0]
	latefee.return_fee = data[1]
	latefee.rental_item = data[2]
	latefee.days_late = data[3]
	latefee.save()

#Create DamageFee
for data in [
	[500.00, hmod.Return.objects.get(id=1), hmod.RentalItem.objects.get(id=1), 'Irreparable damage, cannot be fixed'],
	[5.00, hmod.Return.objects.get(id=1), hmod.RentalItem.objects.get(id=2), 'Tears in the fabric, must be mended'],
	[50.00, hmod.Return.objects.get(id=1), hmod.RentalItem.objects.get(id=3), 'Some broken glass']
]:
	damagefee = hmod.DamageFee()
	damagefee.amount = data[0]
	damagefee.return_fee = data[1]
	damagefee.rental_item = data[2]
	damagefee.description = data[3]
	damagefee.save()

#Create Bulk_Product
for data in [
	['Colonial Honey', '12 oz. of real honey', 'Food', 10.00, 250, hmod.Photograph.objects.get(id=1)],
	['Hand-woven Basket', 'A hand-made basket', 'Misc.', 25.00, 500, hmod.Photograph.objects.get(id=1)]
]:
	bulkproduct = hmod.Bulk_Product()
	bulkproduct.name = data [0]
	bulkproduct.description = data [1]
	bulkproduct.category = data [2]
	bulkproduct.current_price = data [3]
	bulkproduct.quantity_on_hand = data [4]
	bulkproduct.photo = data [5]
	bulkproduct.save()

#Create Indiviudal_Product
for data in [
	['Feather Quill', 'Quill made from eagle’s feather for writing', 'Misc.', 20.00, '1999-07-08 12:00:00', hmod.Photograph.objects.get(id=1)]
]:	
	iproduct = hmod.Individual_Product()
	iproduct.name = data[0]
	iproduct.description = data[1]
	iproduct.category = data[2]
	iproduct.current_price = data[3]
	iproduct.date_made = data[4]
	iproduct.photo = data[5]
	iproduct.save()

#Create Personal_Product
for data in [
	['Personalized Quilt', 'Quilt', 'Misc.', 150.00, 'Personal Quilt', '1999-07-08 12:00:00', hmod.Photograph.objects.get(id=1)]

]:
	pproduct = hmod.Personal_Product()
	pproduct.name = data[0]
	pproduct.description = data[1]
	pproduct.category = data[2]
	pproduct.current_price = data[3]
	pproduct.order_form_name = data[4]
	pproduct.production_time = data[5]
	pproduct.photo = data[6]
	pproduct.save()

#Create OnlinePurchaseOrder
for data in [
	[17.99, hmod.Order.objects.get(id=1)]
]:
	opo=hmod.OnlinePurchaseOrder()
	opo.total = data[0]
	opo.order = data[1]
	opo.save()

#Create OnlinePurchaseProduct
for data in [
	[5, hmod.Product.objects.get(id=1), hmod.OnlinePurchaseOrder.objects.get(id=1)]
]:
	opp = hmod.OnlinePurchaseProduct()
	opp.quantity = data[0]
	opp.product = data[1]
	opp.onlinepurchaseorder = data[2]
	opp.save()