from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import logging

from SETTINGS import settings

class Texter():

	def send_text(self, phone_number, body):

		self.ACCOUNT_SID = settings['ACCOUNT_SID']
		self.AUTH_TOKEN = settings['AUTH_TOKEN']

		self.client = TwilioRestClient(self.ACCOUNT_SID, self.AUTH_TOKEN)

		try:
			self.client.messages.create(
			    to = phone_number,
			    from_ = '9167108744',
			    body = body,
			)
			logging.info("Message sent to phone number: " + phone_number)
		except TwilioRestException as e:
			logging.error("Message could not be sent to phone number " + phone_number)
			logging.error(e)
			raise
	