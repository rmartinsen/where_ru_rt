import requests
import re


def get_time_to_arrival(stop_id, route):

	if stop_id == None:
		stop_id = default_stop_id

	if route == None:
		route = default_route

	html = get_html(stop_id, route)
	minutes_until_arrival = get_time_from_html(html)

	return minutes_until_arrival


def get_html(stop_id, route):
	url = "http://m.sacrt.com/bdetails.aspx?stpid=%s&route=%s" % (stop_id, route)
	print(url)
	html = requests.get(url).text
	return html


def get_time_from_html(html):
	pattern = r'Vehicle [0-9]+ arriving in ([0-9]+) minutes'

	matches = re.search(pattern, html)
	minutes_until_arrival = matches.group(1)

	return minutes_until_arrival
