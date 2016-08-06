from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys

class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        [...]
    @classmethod
    def tearDownClass(cls):
        [...]
    def setUp(self):
        [...]
    def tearDown(self):
        [...]
    def check_for_row_in_list_table(self):
        [...]
