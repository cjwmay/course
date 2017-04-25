from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^destory$', views.destory),
    url(r'^courses/destory/(?P<id>\d+)$', views.confirm),
    url(r'^nodelete$', views.nodelete),
    url(r'^delete$', views.delete),
	url(r'^addcomment$', views.addcomment),
	url(r'^courses/addcomment/(?P<id>\d+)$', views.comment),
]
