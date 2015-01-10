from django.contrib.sitemaps import Sitemap
from portal.models import post

class PostSitemap(Sitemap):
		changefreq = "always"
		priority = 0.5

		def items(self):
			return post.objects.all()

		def lastmod(self, obj):
			return obj.timestamp