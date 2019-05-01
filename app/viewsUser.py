from django.shortcuts import render
from django.http import HttpResponse
from . models import User 
import json

def delete_user(request): 
    body = request.body()
    body_dict = json.loads(body) 
    user_id = body_dict["id"]  
    User.objects.delete(id = user_id)

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
def get_user(request):
	user = User.objects.filter()
	return render(request, 'app/user.html', {'user': user})	


