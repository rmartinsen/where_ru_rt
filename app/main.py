from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main_form():
	return render_template("home.html")

@app.route("/RequestText", methods="POST")
def request_text():
	phone_number = request.form["phone_number"]
	route_number = request.form["route"]
	stop_id = request.form["stop_id"]
	hour = request.form["hour"]
	minute = request.form["minute"]
	max_minutes = request.form["max-minutes"]
	return(phone_number)

if __name__ == "__main__":
	app.run()