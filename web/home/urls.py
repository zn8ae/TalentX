from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [ 
    # ex: /home/
    url(r'^$', views.home, name = 'home'),
    url(r'^homepage', views.home, name = 'home'),
	url(r'^profile/', views.profile,name='profile'),
	#New 
	url(r'^signup/', views.signup,name='signup'),
	url(r'^signin/', views.signin,name='signin'),
	url(r'^signout/', views.signout,name='signout'),
	url(r'^create/', views.create_skill,name='create'),
]
