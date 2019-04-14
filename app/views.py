from django.shortcuts import render
from . models import Product
from . models import Creator 
from django.http import HttpResponse
from . models import Comments
from . models import User 
def add_product(request):
	body = request.body()
	body_dict = json.loads(body)

	name = body_dict["name"]
	creator_id = body_dict["creator_id"]
	prise = body_dict["prise"]
	category =  body_dict["category"]
	date =  body_dict["date"]
	dostup =  body_dict["dostup"]
	creator = Creator.objects.get(id = creator_id)
	product = Product(name = name,prise = prise,
    	category = category,date = date,dostup = dostup,
    	)
	return HttpResponse("всё ок?")
def get_comments(request,product_id = 0):  
    product = Product.objects.get(id = product_id)
    comments = Comments.objects.filter(product = product)
    return HttpResponse(comments)
def delete_user(request): 
    body = request.body()
    body_dict = json.loads(body) 
    user_id = body_dict["id"]  
    User.objects.delete(id = user_id)
def delete_product(request):
	body = request.body()
	body_dict = json.loads(body)
	name = body_dict["name"]
	creator_id = body_dict["creator_id"]
	cost = body_dict["cost"]
	category =  body_dict["category"]
	date =  body_dict["date"]
	dostup =  body_dict["dostup"]
	creator = Creator.objects.delete(id = creator_id)
	product = Product(name = name,prise = prise,
		category = category,date = date,dostup = dostup,
		)
def add_user (request):	 
	body = request.body.decode('utf-8')
	body = body.split("&")

	password = body[0].split("=")[1]
	login = body[1].split("=")[1]
	age = body[2].split("=")[1]

	user = User()
	user.registerUser(login,password,age)

	response = HttpResponse()
	return response
def add_Comments(request):
	body = request.body()
	body_dict = json.loads(body)

	text = body_dict["text"]
	date =  body_dict["date"]
	user = body_dict["user"]
	comments = Comments()	
	response = HttpResponse()
	return response	
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
	return HttpResponse(oder)
def delete_order(request):
	body = request.body()
	body_dict = json.loads(body)
	order_id = body_dict["id"]
	order = Order.objects.delete(id = order_id)
	return HttpResponse(order) 
def delete_comments(request): 
    body = request.body()
    body_dict = json.loads(body) 
    comment_id = body_dict["id"]  
    Comments.objects.delete(id = comments_id)