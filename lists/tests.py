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

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

class SignUpTest(TestCase):
    def test_user_signup(self):
        self.example_user = User.objects.create_user(username='Panachai', password='mypasswordisveryeasy',
                                                     email='panachai@test.com')
        self.example_user.save()

        example_users = User.objects.all()
        self.assertEqual(example_users.count(), 1)