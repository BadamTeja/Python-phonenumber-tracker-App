from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import geocoder, carrier

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    location = ""
    service = ""

    if request.method == "POST":
        number = request.form["number"]

        parsed_number = phonenumbers.parse(number)

        location = geocoder.description_for_number(parsed_number, "en")
        service = carrier.name_for_number(parsed_number, "en")

    return render_template("index.html", location=location, service=service)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5060)
