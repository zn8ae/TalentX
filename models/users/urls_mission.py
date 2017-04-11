from django.conf.urls import url
from . import views

urlpatterns = [ 
    # ex: /users/
    url(r'^create', views.create_mission, name = 'create mission'),
    # url(r'^read', views.lookup_user, name = 'look up a user'),
	url(r'^edit', views.edit_mission, name = 'edit mission'),
	url(r'^delete', views.delete_mission, name = 'delete mission'),
	url(r'^(?P<mission_id>\d+)', views.lookup_mission, name='lookup mission'),
    ]