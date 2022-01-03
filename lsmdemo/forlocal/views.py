from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory  
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .models import *
from .forms import PhoneForm, CreateUserForm, OwnerForm, ShopForm
from .filters import PhoneFilter, HomePhoneFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

def home(request):
	phone = Smartphone.objects.all()
	owner = Owner.objects.all()

	# products = Smartphone.objects.all()
	myFilter = HomePhoneFilter(request.GET, queryset = phone)
	products = myFilter.qs

	context = {'phone': phone, 'owner': owner, 'myfilter': myFilter}
	return render(request, 'home.html', context)

@unauthenticated_user
def signup(request):
	form =  CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			username = form.cleaned_data.get('username')
			group = Group.objects.get(name = 'owner')
			user.groups.add(group)
			Owner.objects.create(
				user=user,
				)

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
	owner  = request.user.owner
	products = owner.smartphone_set.all()

	total_order = products.count()
	# total = orders.filter(status = 'delivered').count()
	available = products.filter(status = 'available').count()
	# ow = Owner.objects.all()
	# id_prdct = Smartphone.objects.all()

	# products = id_prdct.filter(owner = ow)
	# print(owner)
	# owner = Owner.request.user
	# products = Smartphone.objects.filter()

	myFilter = PhoneFilter(request.GET, queryset = products)
	products = myFilter.qs

	context = {'products': products, 'owner': owner, 'total_order': total_order, 'available': available, 'myfilter': myFilter}
	return render(request, 'dashboard.html', context)

# @login_required(login_url = 'Login')
# @allowed_users(allowed_roles = ['owner'])
# def createPhone(request):
# 	OrderFormSet = inlineformset_factory(Owner, Smartphone, fields=('__all__'))
# 	owner = Owner.objects.get(id = request.user.id)
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


# @login_required(login_url = 'Login')
# @allowed_users(allowed_roles = ['owner'])
# def shopProfileSetting(request):
# 	owner = request.user.owner
# 	form = ShopForm(instance = owner.shop)

# 	if request.method == 'POST':
# 		form = ShopForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			# form = form.save(commit = False)
# 			# form.owner_name = Owner.objects.get(user = request.user)
# 			form.save()
# 			return redirect('Shopprofile')

# 	context = {'form': form}
# 	return render(request, 'shop_form.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def shopProfileSetting(request):
	owner = request.user.owner
	form = ShopForm(instance = shop)
	if request.method == 'POST':
		form = ShopForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			form.owner_name = Owner.objects.get(user = request.user)
			form.save()
			return redirect('Shopprofile')

	context = {'form': form}
	return render(request, 'shop_form.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def createPhone(request, pk):
	owne = Owner.objects.get(id = pk)
	form = PhoneForm()

	if request.method == 'POST':

		form = PhoneForm(request.POST)
		# form.instance.owner = request.user
		if form.is_valid():
			print("add")
			form = form.save(commit = False)
			form.owner = Owner.objects.get(user = request.user)
			form.save()
			return redirect('Dashboard')

	context = {'form': form}
	return render(request, 'phone_form.html', context)



@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def updatePhone(request, pk):

	phone = Smartphone.objects.get(id = pk)
	form = PhoneForm(instance = phone)

	if request.method == 'POST':
		form = PhoneForm(request.POST, instance = phone)
		if form.is_valid():
			form.save()
			return redirect('Dashboard')

	context = {'form': form}

	return render(request, 'phone_form.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['owner'])
def deletePhone(request, pk):

	phone = Smartphone.objects.get(id = pk)
	if request.method == 'POST':
		phone.delete()
		return redirect('Dashboard')

	context = {'item': phone}
	return render(request, 'delete.html', context)


def phoneShopDetails(request):
	context = {}
	return render(request, 'phone_shop_view.html', context)