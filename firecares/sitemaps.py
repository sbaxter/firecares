from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class BaseSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
      return['firestation_home', 'login']

    def location(self, item):
        return reverse(item)
