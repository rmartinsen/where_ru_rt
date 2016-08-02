import pymysql
import logging

from SETTINGS import settings

class DBConnection:

	def __init__(self):
		self.host = settings['DB_HOST']
		self.port = settings['DB_PORT']
		self.user = settings['DB_USER']
		self.password = settings['DB_PASSWORD']
		self.db = settings['DB_SCHEMA']

		self.connection = pymysql.connect(host=self.host, 
			port=self.port, user=self.user, 
			password=self.password, db=self.db)

	def run_query(self, query, query_parameters=None):

		self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
		self.cursor.execute(query, query_parameters)

		data = self.cursor.fetchall()

		return(data)

	def get_texts_to_send(self, hour, minute):
		query = """select route_number, stop_id, phone_number, hour, minute, max_minutes
				   from scheduled_texts
				   where hour = %s and minute = %s"""
				   

		parameters = (hour, minute)
		text_messages = self.run_query(query, parameters)

		logging.info(str(len(text_messages)) + " messages found to send" )

		return(text_messages)		
		