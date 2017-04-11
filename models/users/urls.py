from django.conf.urls import url
from . import views

urlpatterns = [ 
    # ex: /users/
    url(r'^create', views.create_user, name = 'insert user'),
	url(r'^edit', views.edit_user, name = 'edit user'),
	url(r'^delete', views.delete_user, name = 'delete user'),
#New 
    url(r'^login/$', views.get_login_info, name='get_login_info'),
    url(r'^auth_create/$', views.auth_create, name='auth_create'),
    url(r'^auth_check/$', views.authenticate, name='authenticate'),
    url(r'^(?P<username>\w+)', views.lookup_user, name='lookup user'),
    ]