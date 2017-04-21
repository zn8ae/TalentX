from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from users import models
from django.views.decorators.csrf import csrf_exempt
import os
import hmac
from django.conf import settings

# Create your views here.

# return JsonResponse({'status':"error", 'msg':"must make POST request"})

@csrf_exempt
def create_skill(request):
	if request.method != 'POST':
		return JsonResponse({'status':"error", 'msg':"must make POST request"})
	if 'sname' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields:sname"})
	username = request.POST.get("username")
	
	s = models.Skill(
		username=request.POST.get("username"),
		sname=request.POST.get("sname"),
		price=request.POST.get("price"),
		desc=request.POST.get("desc")
		)
	s.save()
	return JsonResponse({
		'status':'success',
		'id':s.pk,
		'username':s.username,
		'sname':s.sname,
		'price':s.price
		})

@csrf_exempt
def lookup_skill(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	sid=request.POST.get("sid")
	try:
		s = models.Skill.objects.get(pk=s.pk)
	except models.Mission.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Skill does not exist"})
	return JsonResponse({
		'status':'success',
		'id':s.pk,
		'sname':s.sname, 
		'username':s.username,
		'desc':s.desc,
		'price':s.price,
		})


@csrf_exempt
def create_user(request):
	if request.method != 'POST':
		return JsonResponse({'status':"error", 'msg':"must make POST request"})
	if 'username' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields:username"})
	username = request.POST.get("username")
	try:
		u = models.User.objects.get(username=username)
		return JsonResponse({'status':'error', 'msg':"user already exists!"})
	except models.User.DoesNotExist:
		u = models.User(
			username=request.POST.get("username"),
			first_name=request.POST.get("first_name"),
			last_name=request.POST.get("last_name"),
			email=request.POST.get("email")
			)
		u.save()
		return JsonResponse({'status':'success','user_id': u.pk})

@csrf_exempt
def lookup_user(request, username):
	if request.method != 'GET':
		return JsonResponse({'status':'error', 'msg':"must make GET request"})
	try:
		u = models.User.objects.get(pk=username)
	except models.User.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"User does not exist"})
	return JsonResponse({
		'status':'success',
		'username':u.username, 
		'firstname':u.first_name,
		'lastname':u.last_name,
		'title':u.title,
		'company':u.company,
		'phone':u.phone,
		'email':u.email
		})


@csrf_exempt
def edit_user(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'username' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields"})
	try:
		u = models.User.objects.get(pk=request.POST.get('username'))
	except models.User.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"User does not exist"})

	if 'username' in request.POST:
		u.username = request.POST.get('username')
	if 'first_name' in request.POST:
		u.first_name=request.POST.get("first_name")
	if 'last_name' in request.POST:
		u.last_name=request.POST.get("last_name")
	if 'title' in request.POST:
		u.title=request.POST.get("title")
	if 'company' in request.POST:
		u.company=request.POST.get("company")
	if 'phone' in request.POST:
		u.phone=request.POST.get("phone")
	if 'email' in request.POST:
		u.email=request.POST.get("email")

	u.save()
	return JsonResponse({
		'status':'success',
		'username':u.username, 
		'firstname':u.first_name,
		'lastname':u.last_name,
		'title':u.title,
		'company':u.company,
		'phone':u.phone,
		'email':u.email
		})

@csrf_exempt
def delete_user(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'username' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields"})
	try:
		u = models.User.objects.get(pk=request.POST.get("username"))
	except models.User.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"User does not exist"})
	models.User.delete(u)
	return JsonResponse({'result':"Success"})


# Create your views here.
@csrf_exempt
def create_mission(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'mname' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required field:mname"})
	m = models.Mission(
		mname=request.POST.get("mname"),
		desc=request.POST.get("desc"),
		price=request.POST.get("price"),
		)
	m.save()
	return JsonResponse({'status':'success','mission_id': m.pk})

@csrf_exempt
def lookup_mission(request, mission_id):
	if request.method != 'GET':
		return JsonResponse({'status':'error', 'msg':"must make GET request"})
	try:
		m = models.Mission.objects.get(pk=mission_id)
	except models.Mission.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Mission does not exist"})
	return JsonResponse({
		'id':m.pk,
		'mname':m.mname, 
		'desc':m.desc,
		'price':m.price,
		})


@csrf_exempt
def edit_mission(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'id' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required field:id"})
	try:
		m = models.Mission.objects.get(pk=request.POST.get('id'))
	except models.Mission.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Mission does not exist"})

	if 'mname' in request.POST:
		m.mname = request.POST.get('mname')
	if 'desc' in request.POST:
		m.desc=request.POST.get("desc")
	if 'price' in request.POST:
		m.price=request.POST.get("price")

	m.save()
	return JsonResponse({
		'status':'success',
		'id':m.pk,
		'mname':m.mname,
		'desc':m.desc,
		'price':m.price
		})

@csrf_exempt
def delete_mission(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'id' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required field:id"})
	try:
		m = models.Mission.objects.get(pk=request.POST.get('id'))
	except models.Mission.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Mission does not exist"})
	models.Mission.delete(m)
	return JsonResponse({'result':"Success"})



@csrf_exempt
# Create User Account
def create_account(request):
	if request.method != 'POST':
		return JsonResponse({'status':"error", 'msg':"must make POST request"})
	if 'username' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields:username"})
	if 'password' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields:password"})
	username = request.POST.get("username")
	try:
		acct = models.Account.objects.get(username=username)
		return JsonResponse({'status':'error', 'msg':"account already exists!"})
	except models.Account.DoesNotExist:
		acct = models.Account(
			username=request.POST.get("username"),
			password=request.POST.get("password")
		)
		acct.save()
		return JsonResponse({'status':'success','account_id': acct.pk})

@csrf_exempt
def lookup_account(request, email):
	if request.method != 'GET':
		return JsonResponse({'status':'error', 'msg':"must make GET request"})
	try:
		a = models.Account.objects.get(username=username)
	except models.Account.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Account does not exist"})
	return JsonResponse({
		'status':'success',
		'id':a.pk,
		'username':a.username, 
		'password':a.password
		})


@csrf_exempt
def edit_account(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'id' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields"})
	try:
		a = models.Account.objects.get(pk=request.POST.get('id'))
	except models.Account.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Account does not exist"})

	if 'email' in request.POST:
		a.email = request.POST.get('email')
	if 'password' in request.POST:
		a.password=request.POST.get("password")

	u.save()
	return JsonResponse({
		'status':'success',
		'id':a.pk,
		'email':a.email, 
		'password':a.password
		})

@csrf_exempt
def delete_account(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'id' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields"})
	try:
		a = models.Account.objects.get(pk=request.POST.get('id'))
	except models.Account.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Account does not exist"})
	models.Account.delete(a)
	return JsonResponse({'result':"Success"})

# Authenticator 
def create_authenticator(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'user_id' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields:user_id"})
	auth = models.Authenticator(
		user_id = request.POST.get("user_id"),
		authenticator = request.POST.get("authenticator"),
		date_created = request.POST.get("date_created"),
		)
	u.save()
	return JsonResponse({'status':'success','user_id': auth.pk})

@csrf_exempt
def lookup_account(request, user_id):
	if request.method != 'GET':
		return JsonResponse({'status':'error', 'msg':"must make GET request"})
	try:
		auth = models.Authenticator.objects.get(pk=account_id)
	except models.Authenticator.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Account does not exist"})
	return JsonResponse({
		'status':'success',
		'id':auth.pk,
		'user_id':auth.user_id, 
		'authenticator':auth.authenticator,
		'date':auth.date_created
		})


@csrf_exempt
def edit_account(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'id' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields"})
	try:
		auth = models.Authenticator.objects.get(pk=request.POST.get('id'))
	except models.Authenticator.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Account does not exist"})

	if 'user_id' in request.POST:
		auth.user_id = request.POST.get('user_id')
	if 'authenticator' in request.POST:
		auth.authenticator=request.POST.get("authenticator")
	if 'date_created' in request.POST:
		auth.date_created=request.POST.get("date_created")

	u.save()
	return JsonResponse({
		'status':'success',
		'id':a.pk,
		'user_id':auth.user_id, 
		'authenticator':auth.authenticator,
		'date':auth.date_created
		})

@csrf_exempt
def delete_account(request):
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	if 'id' not in request.POST:
		return JsonResponse({'status':'error', 'msg':"missing required fields"})
	try:
		auth = models.Authenticator.objects.get(pk=request.POST.get('id'))
	except models.Authenticator.DoesNotExist:
		return JsonResponse({'status':'error', 'msg':"Account does not exist"})
	models.Authenticator.delete(a)
	return JsonResponse({'result':"Success"})


#NEW
@csrf_exempt
def get_login_info(request):
	try:
		username = request.POST.get('username')
		m = models.Account.objects.get(username=username)
		pw = m.password
		context={"status":"success", "password":pw}
		return JsonResponse(context)
	except models.Account.DoesNotExist:
		error_msg={"status":"error","msg":"Account Does Not Exist"}
		return JsonResponse(error_msg)

@csrf_exempt
#Check if valid authenticator already existed
def authenticate(request):
	if request.method == 'GET':
		return error_resp(request, "Invalid authenticate request.")
	else:
		# Get user supplied data
		user_email = request.POST.get('email', None)
		user_auth = request.POST.get('authenticator', None)

		# Get authenticator stored in database
		try:
			db_auth_obj = Authenticator.objects.get(authenticator=user_auth)
		except Authenticator.DoesNotExist:
			db_auth_obj = None

		# If it exists, check to see if it's the right one
		if db_auth_obj is not None and db_auth_obj.user_id == user_email:
			return success_resp(request)
		else:
			return error_resp(request, "Invalid authenticate request.")

@csrf_exempt
def generate_auth():
	authenticator = hmac.new(
		key = settings.SECRET_KEY.encode('utf-8'),
		msg = os.urandom(32),
		digestmod = 'sha256',
	).hexdigest()

	return authenticator

@csrf_exempt
# Creates an authenticator for email as ID
def auth_create(request):
	# If GET, bad
	if request.method != 'POST':
		return JsonResponse({'status':'error', 'msg':"must make POST request"})
	# Should be a POST
	else:
		username = request.POST.get('username')
		# Check if user already has an authenticator (check time and update timestamp if "expired")
		auth_exists = models.Authenticator.objects.filter(username = username).exists()
		if auth_exists:
			# auth = Authenticator.objects.get(username = username)
			# if (timezone.now() - auth.date_created).days > 7:
			# 	auth.date_created = timezone.now()
			# auth.save()
			# authenticator = auth.authenticator
			context = {'status':'authExist'}
			return JsonResponse(context)
		else:
			auth = generate_auth()
			#db store auth
			resp = {'auth':auth}
			return JsonResponse(resp)
		