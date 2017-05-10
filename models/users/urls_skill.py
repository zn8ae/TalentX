from django.conf.urls import url
from . import views

urlpatterns = [ 
    # ex: /users/
    url(r'^create', views.create_skill, name='createSkill'),
    url(r'^lookup', views.lookup_skill, name = 'lookupSkill'),
    url(r'^recommend', views.recommend_skill, name = 'recommendSkill'),
	# url(r'^edit', views.edit_mission, name = 'edit mission'),
	# url(r'^delete', views.delete_mission, name = 'delete mission'),
	# url(r'^(?P<skill_id>\d+)', views.lookup_mission, name='lookup mission'),
    ]