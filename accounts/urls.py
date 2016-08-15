from django.conf.urls import url

from accounts import views

urlpatterns = [
    url('^login$',views.persona_login,name='persona_login'),
]
