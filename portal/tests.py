from django.test import TestCase, LiveServerTestCase, Client
from django.contrib.flatpages.models import FlatPage 
from django.contrib.sites.models import Site 

# Create your tests here.
class BaseAcceptanceTest(LiveServerTestCase):
	def setUp(self):
		self.client = Client()

class SitemapTest(BaseAcceptanceTest):
    def test_sitemap(self):
        # Create a post
        # post = postFactory()

        # Create a flat page
        # page = FlatPageFactory()

        # Get sitemap
        response = self.client.get('/sitemap.xml')
        self.assertEquals(response.status_code, 200)

        # Check post is present in sitemap
        self.assertTrue('loren-ipsum-redirect' in response.content)

        # Check page is present in sitemap
        # self.assertTrue('/about/' in response.content)


class FlatPageViewTest(BaseAcceptanceTest):
	
	def test_create_flat_page(self):
        # Create flat page
		page = FlatPage()
		page.url = '/about/'
		page.title = 'About me'
		page.content = 'All about me'
		page.save()

        # Add the site
		page.sites.add(Site.objects.all()[0])
		page.save()

        # Check new page saved
		all_pages = FlatPage.objects.all()
		self.assertEquals(len(all_pages), 1)
		only_page = all_pages[0]
		self.assertEquals(only_page, page)

        # Check data correct
		self.assertEquals(only_page.url, '/about/')
		self.assertEquals(only_page.title, 'About me')
		self.assertEquals(only_page.content, 'All about me')

        # Get URL
		page_url = only_page.get_absolute_url()

        # Get the page
		response = self.client.get(page_url)
		self.assertEquals(response.status_code, 200)

        # Check title and content in response
		self.assertTrue('About me' in response.content)
		self.assertTrue('All about me' in response.content)

