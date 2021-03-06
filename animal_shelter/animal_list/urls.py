from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Animal
from . import views

app_name = 'animal_list'

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Animal.objects.all().order_by('name')[:25],
        template_name="animal_list/list.html"
    )),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Animal,
        template_name="animal_list/details.html"
    )),
    url(r'^adopt/(\d+)/$', views.adopt, name='adopt')
]