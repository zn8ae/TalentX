from django.conf.urls import url
from . import views

urlpatterns = [ 
    # ex: /users/
    url(r'^create', views.create_account, name = 'create account'),
    # url(r'^read', views.lookup_user, name = 'look up a user'),
	url(r'^edit', views.edit_account, name = 'edit account'),
	url(r'^delete', views.delete_account, name = 'delete account'),
	url(r'^(?P<username>\w+)', views.lookup_account, name='lookup account'),
    ]