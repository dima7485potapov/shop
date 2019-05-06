from django.shortcuts import render
from . models import Product
from . models import Creator
from django.http import HttpResponse
import json
from django.db.models import Q

#Получаем страницу с продуктами
def get_products(request):
	#Получаем продукт
	maxPrice = request.GET.get('maxPrice')
	minPrice = request.GET.get('minPrice')
	category = request.GET.get('category')
	order = request.GET.get('order')
	if order == '1':
		order = "prise"
	else:
	    order ="-prise"

	q_objects = Q()
	
	if  type(maxPrice) == int:       
		q_objects.add(Q(prise__lte=int(maxPrice)), Q.AND)
	if  type(minPrice) == int:       
		q_objects.add(Q(prise__gte=int(maxPrice)), Q.AND)
	if type(category) == str:
		q_objects.add(Q(category = category), Q.AND)
	print(q_objects)
	products = Product.objects.order_by(order).filter(q_objects)
	return render(request, 'app/products.html', {'products': products})

def get_product(request,product_id):
	print(product_id)
	product = Product.objects.get(id = product_id)
	return render(request, 'app/product.html', {'product': product})

def add_product(request):
	body_unicode = request.body.decode('utf-8')
	body_dict = json.loads(body_unicode)

	name = body_dict["name"]
	creator_id = body_dict["creator_id"]
	prise = body_dict["prise"]
	category =  body_dict["category"]
	date =  body_dict["date"]
	dostup =  body_dict["dostup"]
	if dostup == 1:
		dostup = True
	else:
		dostup = False

	creator = Creator.objects.get(id = creator_id)

	product = Product(
		name = name,
		prise = prise,
    	category = category,
		date = date,
		dostup = dostup,
		creator = creator
    )

	product.save()
	return HttpResponse("Продукт сохранен!")

def delete_product(request):
	body_unicode = request.body.decode('utf-8')
	body_dict = json.loads(body_unicode)

	product_id = body_dict["id"]
	
	#Удаляем продукт
	Product.objects.delete(id=product_id)
	#Отправляем ответ.
	return HttpResponse("Удалено")