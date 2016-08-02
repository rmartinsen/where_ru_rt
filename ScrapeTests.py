import Scraper

import unittest
from httmock import urlmatch, HTTMock
import requests



class TestScraper(unittest.TestCase):
	
	@urlmatch(netloc="http://m.sacrt.com/bdetails.aspx?stpid=1788&route=38")
	def rt_mock(url, request, other):
		return "testing testing"

	def test_get_html_returns(self):
		with HTTMock(self.rt_mock):
			# html = requests.get('http://google.com').text
			html = requests.get("http://m.sacrt.com/bdetails.aspx?stpid=1788&route=38").text

		self.assertEqual(html, "testing testing")

if __name__ == '__main__':
	unittest.main()