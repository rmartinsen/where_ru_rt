from twilio.rest import TwilioRestClient
from SETTINGS import settings

class Texter():

	def send_text(self, body):

		self.ACCOUNT_SID = settings['ACCOUNT_SID']
		self.AUTH_TOKEN = settings['AUTH_TOKEN']

		self.client = TwilioRestClient(self.ACCOUNT_SID, self.AUTH_TOKEN)

		try:
			self.client.messages.create(
			    to = '9163209285',
			    from_ = '9167108744',
			    body = body,
			)
		except TwilioRestException as e:
			print(e)