from django.urls import path
from .import views

urlpatterns = [
	
	path('', views.home, name = 'Home'),
	path('signup/', views.signup, name = 'Signup'),
	path('signin/', views.signin, name = 'Login'),
	path('logout/', views.logoutpage, name = 'Logout'),
	path('shophome/', views.shopHome, name = 'Shophome'),
	path('dashboard/', views.dashboard, name = 'Dashboard'),
	# path('dashboard/<int:pk>/', views.dashboard, name = 'Dashboard'),
	path('addphone/', views.createPhone, name = 'Addphone'),
	path('profile/', views.profile, name = 'Profile'),
	path('profilesetting/', views.profileSetting, name = 'Profilesetting'),
	path('shopprofile/', views.shopProfile, name = 'Shopprofile'),
	path('shopprofilesetting/', views.shopProfileSetting, name = 'Shopprofilesetting'),

]