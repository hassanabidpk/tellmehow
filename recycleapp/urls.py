from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/product/list/$', views.ProductList.as_view()),
     url(r'^api/v1/product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^api/v1/component/list/$', views.ComponentList.as_view()),
    url(r'^api/v1/component/(?P<pk>[0-9]+)/$', views.ComponentDetail.as_view()),
    url(r'^api/v1/category/list/$', views.CategoryList.as_view()),
    url(r'^api/v1/category/material/(?P<pk>[0-9]+)/$', views.MaterialList.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)