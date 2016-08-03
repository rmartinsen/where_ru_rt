from Scraper import *

import unittest
from httmock import urlmatch, HTTMock
import requests


class TestScraper(unittest.TestCase):

	def setUp(self):
		self.HTML = """blah blah blah
						<div>Vehicle 3815 arriving in 7 minutes </div>
						blah blah blah"""
	
	# @urlmatch(netloc=r"http:\/\/m\.sacrt\.com/bdetails\.aspx\?stpid=1788&route=38$")
	def rt_mock(self, url, request):
		return "testing testing"

	def test_get_html_returns(self):
		with HTTMock(self.rt_mock):
			# html = requests.get('http://google.com').text
			html = requests.get("http://m.sacrt.com/bdetails.aspx?stpid=1788&route=38").text

	def test_get_time_from_html(self):
		minutes_to_arrival = get_time_from_html(self.HTML)
		self.assertEqual('7', minutes_to_arrival)

	def test_get_time_to_arrival_all_parameters(self):
		mock_html = unittest.MagicMock(return_value=3)
		self.assertEqual(mock_html(), 3)





if __name__ == '__main__':
	unittest.main()