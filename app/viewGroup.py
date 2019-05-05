from django.shortcuts import render
from . models import Group
from django.http import HttpResponse
import json


def get_group(request):  
    group = Group.objects.filter(group = group)
    return HttpResponse(group)

def add_group(request):
	body = request.body()
	body_dict = json.loads(body)
	name = body_dict["text"]
	plus_tovar =  get_bool(int(plus_tovar))
	minus_tovar = get_bool(int(minus_tovar))
	plus_user = get_bool(int(plus_user))
	minus_user = get_bool(int(minus_user))
	plus_comments = get_bool(int(plus_comments)) 
    group = Group(name = name,
    	          plus_tovar = plus_tovar,
                  plus_user = plus_user,
                  plus_comments = plus_comments,
                  minus_user = minus_user,
    	          minus_tovar = minus_tovar)
    group.save()
	return HttpResponse(group)

def delete_group(request): 
    body = request.body()
    body_dict = json.loads(body) 
    group_id = body_dict["id"]  
    Group.objects.delete(name = name)

def get_bool(a):
	if a == 1:
		a = True
	else:
		a = False

