from django.conf.urls import url, include
from django.conf.urls.static import static
from .apis import BlogpostSet
from rest_framework import routers
from django.contrib.sitemaps.views import sitemap
from .sitemap.sitemaps import PageSitemap,FlatPageSitemap, BlogSitemap
from . import views

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost',BlogpostSet, 'Blogpost')

sitemaps = {
    "page": PageSitemap,
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<slug>[^\.]+)', views.view_post, name='view_blog_post'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(apiRouter.urls)),
    ]
