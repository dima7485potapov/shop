from django.shortcuts import render
from . models import Comments
from . models import User 
from . models import Product
from django.http import HttpResponse
import json

def get_comments(request,product_id = 0):  
    product = Product.objects.get(id = product_id)
    comments = Comments.objects.filter(product = product)
    return HttpResponse(comments)

def add_Comments(request):
	body = request.body()
	body_dict = json.loads(body)

	text = body_dict["text"]
	date =  body_dict["date"]
	user = body_dict["user"]
	comments = Comments()	
	response = HttpResponse()
	return response	

def delete_comments(request): 
    body = request.body()
    body_dict = json.loads(body) 
    comment_id = body_dict["id"]  
    Comments.objects.delete(id = comment_id)