from twilio.rest import TwilioRestClient
from SETTINGS import settings

ACCOUNT_SID = settings['ACCOUNT_SID']
AUTH_TOKEN = settings['AUTH_TOKEN']

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

try:
	client.messages.create(
	    to = '9163209285',
	    from_ = '9167108744',
	    body = 'Hello, the Mambo',
	)
except TwilioRestException as e:
	print(e)