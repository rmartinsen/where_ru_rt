#!/usr/bin/python3

from TextSender import Texter
from Scraper import get_time_to_arrival

default_stop_id = 1788
default_route = 38

if __name__ == '__main__':

	arrival_time = get_time_to_arrival(default_stop_id, default_route)

	if arrival_time:
		texter = Texter()
		texter.send_text("Bus on route " + str(default_route) + 
			" will arrive at bus stop " + str(default_stop_id) +
			" in " + str(arrival_time) + " minutes")
		



