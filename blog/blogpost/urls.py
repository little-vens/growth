from django.conf import settings
from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<slug>[^\.]+)', views.view_post, name='view_blog_post'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    ]
