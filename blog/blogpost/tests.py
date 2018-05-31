from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase, LiveServerTestCase
from datetime import datetime
from .views import index, view_post
from .models import Blogpost
from selenium import webdriver
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class HomepageTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver.exe'))
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_visit_homepage(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/blogpost/")
        )

        self.assertIn("Welcome to my blog", self.selenium.title)