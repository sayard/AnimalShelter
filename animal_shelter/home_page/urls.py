from django.conf.urls import url
from . import views

app_name = 'home_page'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login_user')
]
