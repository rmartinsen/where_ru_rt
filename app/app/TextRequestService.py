from random import randint
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from twilio import TwilioRestException

from app.TextSender import Texter
from app.orm import ScheduledText

from SETTINGS import settings


def send_confirmation_text(scheduled_text):
	validation_code = scheduled_text.validation_code
	phone_number = scheduled_text.phone_number

	text_body = "Your confirmation code is %s" % validation_code

	texter = Texter()
	texter.send_text(phone_number, text_body)


def activate_scheduled_text(text_data):
	engine = create_engine(settings['ENGINE_STRING'])
	session = Session(engine)

	try:
		scheduled_text_id = text_data['scheduled_text_id']

		scheduled_text = session.query(ScheduledText).get(scheduled_text_id)

		entered_validation_code = text_data['validation_code']
		db_validation_code = str(scheduled_text.validation_code)

		if entered_validation_code == db_validation_code:
			scheduled_text.is_validated = 1
			session.commit()
			return True
		else:
			return False

	except:
		session.rollback()
		raise


def create_scheduled_text(text_data):
	engine = create_engine(settings['ENGINE_STRING'])
	session = Session(engine)

	try:
		st = ScheduledText()

		validation_code = randint(100000,999999)
		
		st.phone_number = text_data["phone_number"]
		st.route_number = text_data["route_number"]
		st.stop_id =	  text_data["stop_id"]
		st.hour =		  text_data["hour"]
		st.minute =	   	  text_data["minute"]
		st.max_minutes =  text_data["max_minutes"]
		st.validation_code = validation_code

		session.add(st)
		session.commit()

	except:
		session.rollback()
		raise

	return st