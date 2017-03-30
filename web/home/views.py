from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
import requests
from .forms import SignInForm, SignUpForm, CreateSkillForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import check_password, make_password
from django.urls import reverse

# Create your views here.
@csrf_exempt
def home(request):
	# make http call urllib, requests
	username='Zihan'
	r = requests.get('http://exp-api:8000/userdata/'+username)
	data = r.json()

	# d = {"person": {"first_sname": "Joe", "last_name": "Johnson"}}
	return render_to_response('templates/homepage.html',data)

@csrf_exempt
def profile(request):
	username='Zihan'
	r = requests.get('http://exp-api:8000/userdata/' + username)
	data = r.json()
	
	return render_to_response('templates/profile.html',data)

@csrf_exempt
def signup(request):
	error = None
	if request.method=="POST":
		form = request.POST
		# verify form information here
		validate_form = SignUpForm(form)
		if validate_form.is_valid() and form["password"]==form["password2"]:
			# make exp call
			username=form["username"]
			first_name=form["first_name"]
			last_name=form["last_name"]
			email=form["email"]
			password=make_password(form["password"])
			context={'username':username,'first_name':first_name,'last_name':last_name,'email':email,'password':password}
			r = requests.post('http://exp-api:8000/userdata/create/', context)
			resp = r.json()

			if resp["account"]["status"]=="error" or resp["user"]["status"]=="error":
				error="account or user already exists!"
			else:
				return render(request, 'templates/register_success.html')
		else:
			if form["password"]!=form["password2"]:
				error="unmatched password"
			else:
				error="missing required fields"
			return render(request, 'templates/signup.html', {'form': validate_form, 'error': error})

	form=SignUpForm()
	if error!=None:
		return render(request, 'templates/signup.html', {'form': validate_form, 'error':error})
	else:
		return render(request, 'templates/signup.html', {'form': form})
		# return HttpResponse("POST")


@csrf_exempt
def signin(request):
	# auth = request.COOKIES.get('auth')
	# if auth:
	# 	response = HttpResponseRedirect("/homepage")
	# else 

	error = None
	if request.method == 'GET':
		form = SignInForm()
		return render(request, 'templates/signin.html',  {'form': form, 'error':error})

	if request.method == 'POST':
		form = SignInForm(request.POST)

		if not form.is_valid():
			error = "form not valid"
			return render(request,'templates/signin.html',  {'form': form, 'error':error})

		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		
		post_data = {
			'username' : username,
			'password' : password
		}

		try:
			resp = requests.post('http://exp-api:8000/userdata/signin/', data = post_data)
			result = resp.json()
			if(result["status"]=="error"):
				error = result["msg"]
				return render(request,'templates/signin.html',  {'form': form, 'error':error})
			else:
				response = HttpResponseRedirect(reverse('create'))
				response.set_cookie("auth", result["auth"])
				# return JsonResponse(result)
				return response

			# if(result["status"]=="error"):
			# 	error = result["msg"]
			# 	return render(request,'templates/signin.html',  {'form': form, 'error':error})
			# else:
			# 	#generate authenticator 
			# 	#store authenticator in coolkie

		except requests.exceptions.RequestException as e:
			return HttpResponse("request exception")
		
		# else:
		# 	if not resp:
		# 		error = "No response"
		# 		return render(request, 'templates/signup.html', {'form': form, 'error':error})		
		# 	else:
		# 		authenticator = resp.json()['auth']
  #   			#Redirect to a page 
		# 		response = redirect('home')
		# 		response.set_cookie("auth", authenticator)
		# 		return response
		# 		#return HttpResponse(resp)

@csrf_exempt
def signout(request):
	response = HttpResponseRedirect("/homepage")
	#return HttpResponse("POST")	
	response.delete_cookie("auth")
	return response

@csrf_exempt
def create(request):
	auth = request.COOKIES.get('auth')
	if auth:
		return render_to_response('templates/create.html')
	else:
		return render_to_response('templates/signup.html')

@csrf_exempt
def create_skill(request):
	error = None

	auth = request.COOKIES.get('auth')
	if not auth: 
		form = SignInForm
		return HttpResponseRedirect(reverse('signin'))

	if request.method=="POST":
		form = request.POST
		# verify form information here
		validate_form = CreateSkillForm(form)
		if validate_form.is_valid() :
			# make exp call
			skill = form["skill"]
			price = form["price"]
			desc = form["desc"]
			context={
			'skill': skill,
			'price':price,
			'desc':desc
			}
			#r = requests.post('http://exp-api:8000/userdata/create/', data=context)
			r = requests.post('http://exp-api:8000/userdata/createSkill/', data=context)
			result=r.json()
			if(result["status"]=="error"):
				error = result["msg"]
				return render(request,'templates/create.html',  {'form': validate_form, 'error':error}) 
			return render(request,'templates/skill_success.html')
			#return render(request, 'templates/register_success.html')
		else:
			return render(request, 'templates/create.html', {'form': validate_form, 'error':error})
	form = CreateSkillForm()
	if error!=None:
		return render(request, 'templates/create.html', {'form': form, 'error':error})
	else:
		return render(request, 'templates/create.html', {'form': form})
		# return HttpResponse("POST")