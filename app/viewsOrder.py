from django.shortcuts import render
from . models import Order
from . models import Product
from . models import User
from django.http import HttpResponse
import json

def add_order(request):
	body = request.body()
	body_dict = json.loads(body)
	product_id = body_dict["product_id"]
	user_id = body_dict["user_id"]	
	date =  body_dict["date"]
	cost = body_dict["cost"]
	state =  body_dict["state"]
	product = Product.objects.get(id = product_id)
	user = User.objects.get(id = user_id)
	order = Order(date = date,cost = cost,state = state,product = product,user = user)
	order.save()
	return HttpResponse(order)

def delete_order(request):
	body = request.body()
	body_dict = json.loads(body)
	order_id = body_dict["id"]
	order = Order.objects.delete(id = order_id)
	return HttpResponse(order) 
def get_order(request):
	#Получаем продукт
	order = Order.objects.filter()

	#Отправляем
	return render(request, 'app/order.html', {'order': order})	