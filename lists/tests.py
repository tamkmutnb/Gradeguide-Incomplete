from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from django.test import TestCase
from lists.models import Item

from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_student_status(self):
        submit_text = self.browser.find_element_by_id('gradeshow').text
        if self.assertIn('2.5', submit_text):
            self.assertIn('Normal State', submit_text)
        elif self.assertIn('1.5', submit_text):
            self.assertIn('Retired', submit_text)
        elif self.assertIn('2', submit_text):
            self.assertIn('Probation', submit_text)