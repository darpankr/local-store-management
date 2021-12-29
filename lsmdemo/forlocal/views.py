from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory  
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

def home(request):
	phone = Smartphone.objects.all()
	owner = Owner.objects.all()

	context = {'phone': phone, 'owner': owner}
	return render(request, 'home.html', context)

@unauthenticated_user
def signup(request):
	form =  CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			# username = orm.cleaned_data.get('username')
			# group = Group.objects.get(name = 'customer')
			# user.groups.add(group)
			# Customer.objects.create(
			# 	user=user,
			# 	)

			# messages.success(request, 'Account was created for ' + username)
			return redirect('Login')

	context = {'form': form}
	return render(request, 'signup.html', context)
	
@unauthenticated_user
def signin(request):
    if request.method == 'POST':
    	username = request.POST.get('username')
    	password = request.POST.get('password')

    	user = authenticate(request, username = username, password = password)
    	if user is not None:
    		login(request, user)
    		return redirect('Shophome')
    	else:
    		messages.info(request, 'Username or Password is incorrect ')
    context = {}
    return render(request, 'login.html', context)
 
def logoutpage(request):
	logout(request)
	return redirect('Home')


# def signup(request):

# 	context = {}

# 	return render(request, 'base.html', context)

# def login(request)
# :
# 	context = {}

# 	return render(request, 'login.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner', 'admin'])
def shopHome(request):
	context = {}
	return render(request, 'shop_home.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def dashboard(request):
	owner = request.user.owner
	products = Smartphone.objects.filter(owner_id = owner)
	# print(owner)
	# owner = Owner.request.user
	# products = Smartphone.objects.filter()
	context = {'products': products}
	return render(request, 'dashboard.html', context)

# @login_required(login_url = 'Login')
# def createPhone(request):
# 	OrderFormSet = inlineformset_factory(Shop, Smartphone, fields=('__all__'), extra=5)
# 	# owner = Owner.objects.get(id = pk)
# 	formset = OrderFormSet(queryset=Smartphone.objects.none())
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		#form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('Dashboard')

# 	context = {'formset':formset}
# 	return render(request, 'phone_form.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def createPhone(request):
	owner = request.user.id
	owner_id = Smartphone.objects.get(id = owner)
	form = PhoneForm()

	if request.method == 'POST':
		form = PhoneForm(request.POST, instance = owner_id)
		if form.is_valid():
			print("add")
			form.save()
			return redirect('Dashboard')

	context = {'form': form}
	return render(request, 'phone_form.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def profile(request):
	owner = request.user.owner

	context = {'owner': owner}
	return render(request, 'profile.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def profileSetting(request):
	owner = request.user.owner
	form = OwnerForm(instance = owner)

	if request.method == 'POST':
		form = OwnerForm(request.POST, request.FILES, instance = owner)
		if form.is_valid():
			form.save()
			return redirect('Profile')

	context = {'form': form}
	return render(request, 'profile_form.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def shopProfile(request):
	owner = request.user.owner

	context = {'owner': owner}
	return render(request, 'shop_profile.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def shopProfileSetting(request):
	owner = request.user.owner.shop
	form = ShopForm(instance = owner)

	if request.method == 'POST':
		form = ShopForm(request.POST, request.FILES, instance = owner)
		if form.is_valid():
			form.save()
			return redirect('Shopprofile')

	context = {'form': form}
	return render(request, 'shop_form.html', context)