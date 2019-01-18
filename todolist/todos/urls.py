from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^add", views.add, name="add"),
    # url(r'^(?P<pk>[0-9]+)/delete/$',views.delete),
    url(r"^(?P<pk>[0-9]+)/change/$", views.edit),
    url(r"^(?P<pk>[0-9]+)/detail/$", views.detail),
    url(r"^(?P<pk>\d+)/delete/$", views.delete, name="delete"),
]
