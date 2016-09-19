from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.
class StudentViewTests(Testcast):
	def test_views_index(self):
		index_url = reverse('student:index')
		self.client.get(index_url)
		self.assertEqual(response.status_code, 200)