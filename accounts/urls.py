from django.conf.urls import url
from django.contrib.auth import views as vi
from accounts import views

urlpatterns = [
    url('^login$',views.persona_login,name='persona_login'),
    url('^logout$',vi.logout,{'next_page':'/'},name='logout'),
]
