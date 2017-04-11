from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
from elasticsearch import Elasticsearch
from kafka import KafkaProducer
import json


# Create your views here.
@csrf_exempt
def userdata(request, username):
	# make http call urllib, requests
	try:
		u = requests.get('http://models-api:8000/users/'+ username)
		m = requests.get('http://models-api:8000/missions/1')
		m2 = requests.get('http://models-api:8000/missions/2')
		context = {'users':u.json(),'mission':m.json(),'mission2':m2.json()}
		
	except requests.exceptions.ConnectionError:
		return HttpResponse("Connection Error")

	return JsonResponse(context)

@csrf_exempt
def create(request):
	data=request.POST.copy()
	userdata={'username':data["username"],'email':data["email"],'first_name':data["first_name"],'last_name':data["last_name"]}
	u = requests.post('http://models-api:8000/users/create',userdata)

	acctdata={'username':data["username"],'password':data['password']}
	a = requests.post('http://models-api:8000/accounts/create',acctdata)

	context={'user':u.json(), 'account':a.json()}
	return JsonResponse(context)
    
@csrf_exempt
def createSkill(request):
    context = request.POST.copy()
    skill=context["skill"]
    price=context["price"]
    desc=context["desc"]
    skilldata = {'sname':skill,'price':price,'desc':desc,'username':'Zihan'}
    r = requests.post('http://models-api:8000/skills/create',skilldata)
    response = r.json()
    kp = KafkaProducer(bootstrap_servers='kafka:9092')
    kp.send('new-listings-topic', json.dumps(response).encode('utf-8'))
    return JsonResponse(response)
#New
@csrf_exempt
def signin(request):
    if request.method == 'GET':
        return error_resp(request, "Invalid login request.")

    if request.method == 'POST':
        # get the post data for email and password
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')

        context={"username":user_username, "password":user_password}

        r = requests.post('http://models-api:8000/users/login/',context)
        # return HttpResponse(r)
        login_json=r.json()

        if login_json['status'] == 'error':
            resp = {"status":'error',"msg":login_json["msg"]}
            return JsonResponse(resp)
        else:
            #user account exists, check password
            db_password = login_json["password"]
            if check_password(user_password, db_password):
                #check authenticator
                user={"username":user_username}
                p = requests.post('http://models-api:8000/users/auth_create/',user)
                resp = {"status":"success", "auth":p.json()["auth"]}
                return JsonResponse(resp)
            else:
                return JsonResponse({"status":"error","msg":"Incorrect Password"})

@csrf_exempt
def search(request):
    #return HttpResponse(request.POST.get('search'))   
    es = Elasticsearch(['es'])
    s = request.POST.get('search')
    results = es.search(index='listing_index', body={'query': {'query_string': {'query': s}}, 'size': 10})
    search_results = {
        'result': [hit['_source'] for hit in results['hits']['hits']],
    }
    return JsonResponse(search_results)
