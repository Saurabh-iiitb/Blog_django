from django.test import TestCase
from .models import Post, Author, Category

# Create your tests here.

class CategoryModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Category.objects.create(title='firstPost') 

	def test_title_label(self):
		post = Category.objects.get(id=1)
		field_label = post._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'title')

	def test_first_name_max_length(self):
		author = Category.objects.get(id=1)
		max_length = author._meta.get_field('title').max_length
		self.assertEquals(max_length, 20)
