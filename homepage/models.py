
from django.db import models
from django.contrib.auth.models import AbstractUser
import django.contrib.auth.models

class Address(models.Model):
	address_1 = models.TextField()
	address_2 = models.TextField(null=True)
	city = models.TextField()
	state = models.TextField()
	zip = models.IntegerField()

	def __str__(self):
		pass

class Photograph(models.Model):
	date_taken = models.DateField()
	place_taken = models.TextField(null=True)
	image = models.TextField()
	caption = models.TextField(null=True)

	def __str__(self):
		pass

class Organization(models.Model):
	name = models.TextField()
	organization_type = models.TextField()
	address = models.ForeignKey(Address)

	def __str__(self):
		pass

class User(AbstractUser):
	birth_date = models.DateField(null=True)
	address = models.ForeignKey(Address, null=True)
	organization = models.ForeignKey(Organization, null=True)

	def __str__(self):
		pass

	def getEmail(username):
		pass

class Agent(User):
	appointment_date = models.DateTimeField()

class Venue(models.Model):
	name = models.TextField()
	photo = models.ForeignKey(Photograph, null=True)
	address = models.ForeignKey(Address)

	def __str__(self):
		pass

class Event(models.Model):
	event_name = models.TextField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	map_file_name = models.FilePathField(null=True)
	public_event = models.BooleanField(default=False)
	venue = models.ForeignKey(Venue)

	def __str__(self):
		pass

class Area(models.Model):
	name = models.TextField()
	description = models.TextField(null=True)
	place_number = models.IntegerField()
	coordinator = models.ForeignKey(Agent, related_name='+')
	supervisor = models.ForeignKey(Agent, related_name='+')
	event = models.ForeignKey(Event)

	def __str__(self):
		pass

class AreaProduct(models.Model):
	name = models.TextField()
	description = models.TextField()
	low_price = models.DecimalField(max_digits=10, decimal_places=2)
	high_price = models.DecimalField(max_digits=10, decimal_places=2)
	area = models.ForeignKey(Area)

	def __str__(self):
		pass

class Participant(User):
	biographical_sketch = models.TextField(null=True)
	contact_relationship = models.TextField()
	e_contact_name = models.TextField()
	e_contact_phone = models.TextField()
	photo = models.ForeignKey(Photograph, null=True)

	def __str__(self):
		return self.biographical_sketch

class Role(models.Model):
	name = models.TextField()
	type = models.TextField()
	participant = models.ForeignKey(Participant)
	area = models.ForeignKey(Area)

	def __str__(self):
		pass

class Item(models.Model):
	name = models.TextField()
	description = models.TextField(null=True)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	standard_rental_price = models.DecimalField(max_digits=10, decimal_places=2)
	is_rentable = models.BooleanField(default=False)
	user = models.ForeignKey(User)
	photo = models.ForeignKey(Photograph, null=True)

	def __str__(self):
		return self.name

	def lookup(ItemID):
		pass

	def isRentable(ItemID):
		pass

	def itemAvailable(ItemID):
		pass

class Wardrobe_Item(Item):
	size = models.TextField()
	size_modifier = models.TextField(null=True)
	gender = models.TextField()
	color = models.TextField()
	pattern = models.TextField()
	start_year = models.IntegerField()
	end_year = models.IntegerField()
	note = models.TextField(null=True)

class Order(models.Model):
	order_date = models.DateTimeField()
	phone = models.BigIntegerField(null=True)
	date_packed = models.DateTimeField(null=True)
	date_paid = models.DateTimeField(null=True)
	date_shipped = models.DateTimeField(null=True)
	tracking_number = models.BigIntegerField(null=True)
	online_order = models.BooleanField(default=True)
	in_person_pickup = models.BooleanField(default=False)
	packed_by = models.ForeignKey(Agent, null=True, related_name='+')
	shipped_by = models.ForeignKey(Agent, null=True, related_name='+')
	processed_by = models.ForeignKey(Agent, null=True, related_name='+')
	customer = models.ForeignKey(User)
	ships_to = models.ForeignKey(Address, null=True)
	payment = models.TextField()
	def __str__(self):
		pass

	def getOrderObjects(orderID):
		pass

	def getUser(OrderID):
		pass

class Rental(models.Model):
	rental_time = models.DateTimeField(null=True)
	due_date = models.DateTimeField(null=True)
	discount_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	order = models.ForeignKey(Order, null=True)

	def __str__(self):
		pass

	def getOverdueRentalItems(RentalID):
		pass

	def getOrder(RentalID):
		pass

class Return(models.Model):
	return_time = models.DateTimeField()
	fees_paid = models.BooleanField(default=False)
	agent = models.ForeignKey(Agent)
	#payment = models.ForeignKey(Payment, null=True)
	rental = models.ForeignKey(Rental)

	def __str__(self):
		pass

	def addFee(Fee):
		pass

	def checkReturned(RentalID):
		pass

	def getRentalItems(RentalID):
		pass

class RentalItem(models.Model):
	rental_id = models.ForeignKey(Rental)
	item_id = models.ForeignKey(Item)
	returns = models.ForeignKey(Return, null=True)

	def __str__(self):
		pass

	def getItem(ItemID):
		pass

	def getReturnedInfo(ItemID):
		pass

	def lookup(RentalID):
		pass

class Fee(models.Model):
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	return_fee = models.ForeignKey(Return, null=True)
	rental_item = models.ForeignKey(RentalItem, null=True)

	def __str__(self):
		pass

class LateFee(Fee):
	days_late = models.IntegerField()

class DamageFee(Fee):
	description = models.TextField()

class Product(models.Model):
	name = models.TextField()
	description = models.TextField(null=True)
	category = models.TextField(null=True)
	current_price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name

	def viewAvailability(product_id):
		pass

class Bulk_Product(Product):
	quantity_on_hand = models.IntegerField()
	photo = models.ForeignKey(Photograph, null=True)

class Individual_Product(Product):
	date_made = models.DateTimeField()
	photo = models.ForeignKey(Photograph, null=True)

class Personal_Product(Product):
	order_form_name = models.TextField()
	production_time = models.DateTimeField()
	photo = models.ForeignKey(Photograph, null=True)

class OnlinePurchaseOrder(models.Model):
	total = models.IntegerField(null=True)
	order = models.ForeignKey(Order, null=True)

	def __str__(self):
		pass

	def lookup(id):
		pass

class OnlinePurchaseProduct(models.Model):
	quantity = models.IntegerField()
	product = models.ForeignKey(Product)
	onlinepurchaseorder = models.ForeignKey(OnlinePurchaseOrder)

	def __str__(self):
		pass

	def lookup(id):
		pass
