from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from ..models import Blogpost
from django.apps import apps as django_apps

class PageSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
class BlogSitemap(Sitemap):

    priority = 0.5
    changefreq = 'never'

    def items(self):
        return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.posted

class FlatPageSitemap(Sitemap):
    priority = 0.8

    def items(self):
        Site = django_apps.get_model('sites.Site')
        current_site = Site.objects.get_current()
        return current_site.flatpage_set.filter(registration_required=False)
