from flask import Flask, flash, render_template, redirect, request
from app.TextRequestService import activate_scheduled_text, create_scheduled_text, send_confirmation_text
from twilio import TwilioRestException

app = Flask(__name__)
app.secret_key = 'adsfkhasdfhadlf'

@app.route("/")
def main_form():
	return render_template("home.html")


@app.route("/RequestText", methods=["POST"])
def request_text():
	st = create_scheduled_text(request.form)

	try:
		send_confirmation_text(st)
		return render_template("validation_text.html",
								phone_number=st.phone_number,
								scheduled_text_id = st.scheduled_text_id)

	except TwilioRestException as e:
		return render_template("text_error.html",
								phone_number=st.phone_number)


@app.route("/CheckValidationCode", methods=["POST"])
def check_validation():
	if activate_scheduled_text(request.form):
		return redirect("/Success")
	else:
		flash("We were unable to confirm using that validation code. Please try again")
		return render_template("validation_text.html",
						   phone_number=request.form['phone_number'],
						   scheduled_text_id=request.form['scheduled_text_id'])

@app.route("/Success")
def success():
	return render_template("success.html")

if __name__ == "__main__":
	app.run(debug=True)