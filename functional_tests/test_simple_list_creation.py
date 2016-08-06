from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        [...]

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        [...]

class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        [...]
