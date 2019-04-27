from django.db import models
import django

class Creator(models.Model):
	name = models.CharField(max_length=125)
	address = models.CharField(max_length = 40)
	phone = models.CharField(max_length = 11)		

class Product(models.Model):
	name = models.CharField(max_length=80)
	creator = models.ForeignKey("Creator",on_delete=models.CASCADE)
	prise = models.FloatField(null = False)
	category = models.CharField(max_length = 20)
	date = models.DateField()
	dostup = models.BooleanField()

class User(models.Model):
	name = models.CharField(max_length=125)
	date_of_registration = models.DateField()
	group = models.ForeignKey("Group",on_delete=models.CASCADE)

class Group(models.Model):
	name = models.CharField(max_length=125)
	plus_tovar = models.BooleanField()
	minus_tovar = models.BooleanField()
	plus_user = models.BooleanField()
	minus_user = models.BooleanField()
	plus_coments = models.BooleanField()

class Comments(models.Model):
	text = models.CharField(max_length=125)
	date = models.DateField(default =django.utils.timezone.now)
	product = models.ForeignKey("Product",on_delete=models.CASCADE)    
	user = models.ForeignKey("User",on_delete=models.CASCADE)

class Order(models.Model):
	product = models.ForeignKey("Product",on_delete=models.CASCADE)    
	date = models.DateField(default =django.utils.timezone.now)
	cost = models.FloatField()    
	state = models.CharField(max_length=125)	
	user = models.ForeignKey("User",on_delete=models.CASCADE)