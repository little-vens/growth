from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase, LiveServerTestCase
from datetime import datetime
from .views import index, view_post
from .models import Blogpost
from selenium import webdriver


class HomepageTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_visit_homepage(self):
        self.selenium.get(
            '%s%s' % self.live_server_url, "blogpost/"
        )

        self.assertIn("Welcome to my blog", self.selenium.title)