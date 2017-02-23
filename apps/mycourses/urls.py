from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^add$', views.add),
  url(r'^detail/(?P<id>\d+)/?$',views.detail),
  url(r'^delete/(?P<id>\d+)/?$',views.delete),
]
