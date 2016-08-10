from Scraper import *
from TextSender import *

import unittest
from unittest.mock import MagicMock, patch
import httpretty
import requests


class TestScraper(unittest.TestCase):

	def setUp(self):
		self.url = "http://m.sacrt.com/bdetails.aspx?stpid=1788&route=38"
		self.HTML = """blah blah blah
						<div>Vehicle 3815 arriving in 7 minutes </div>
						blah blah blah"""
		httpretty.enable()
		httpretty.register_uri(httpretty.GET, self.url, status=200, body=self.HTML)

	def tearDown(self):
		httpretty.disable()

	def test_get_time_to_arrival_all_parameters(self):
		mock_html = MagicMock(return_value=3)
		self.assertEqual(mock_html(), 3)

	def test_get_html_returns_html(self):
		HTML = get_html(1788, 38)
		self.assertEqual(HTML, self.HTML)

	def test_get_time_from_html(self):
		minutes_to_arrival = get_time_from_html(self.HTML)
		self.assertEqual('7', minutes_to_arrival)

class TestTexter(unittest.TestCase):
	@patch.object(TextSender)
	def test_msg_sent(self):
		v




if __name__ == '__main__':
	unittest.main()