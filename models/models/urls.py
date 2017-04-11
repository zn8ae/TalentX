from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^users/', include('users.urls')),	
	url(r'^missions/', include('users.urls_mission')),	
	url(r'^accounts/', include('users.urls_account')),	
	url(r'^skills/', include('users.urls_skill')),
]
