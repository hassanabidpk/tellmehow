from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/product/list/$', views.ProductList.as_view()),
    url(r'^api/v1/product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^api/v1/product/code/(?P<code>[a-zA-Z0-9]+)/$', views.ProductDetailFromCode.as_view()),
    url(r'^api/v1/component/list/$', views.ComponentList.as_view()),
    url(r'^api/v1/component/(?P<pk>[0-9]+)/$', views.ComponentDetail.as_view()),
    url(r'^api/v1/category/list/$', views.CategoryList.as_view()),
    url(r'^api/v1/category/material/(?P<pk>[0-9]+)/$', views.MaterialList.as_view()),
    url(r'^api/v1/category/component/(?P<pk>[0-9]+)/$', views.ComponentDetailFromMaterial.as_view()),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)