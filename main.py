#!/usr/bin/python3
from datetime import datetime
import logging

from TextSender import Texter
from Scraper import get_time_to_arrival
from DB import DBConnection



if __name__ == '__main__':

	logging.basicConfig(filename='rurt.log', 
						level=logging.INFO,
						format='%(asctime)s %(message)s')

	now = datetime.now()

	now_hour = now.hour
	now_minute = now.minute

	logging.info("Beginning process: Hour = " + str(now_hour) + ", minute = " + str(now_minute))

	conn = DBConnection()

	texts_to_send = conn.get_texts_to_send(now_hour, now_minute)

	for text_msg in texts_to_send:
		arrival_time = get_time_to_arrival(text_msg['stop_id'], text_msg['route_number']) 

		phone_number = text_msg['phone_number']

		texter = Texter()
		texter.send_text(phone_number, "Bus on route " + text_msg['route_number'] + 
			" will arrive at bus stop " + str(text_msg['stop_id']) +
			" in " + str(arrival_time) + " minutes")

	logging.info("Ending process: Hour = " + str(now_hour) + ", minute = " + str(now_minute))



