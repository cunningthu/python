import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():

    # Query for currency exchange render_template
    currency = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest?access_key=5deecb6c00ede7c2ff33be1626d749cc",
                        params={"symbols":currency})

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})

    # Make sure currency is in response
    data = res.json()
    try:
        if currency not in data["rates"]:
            return jsonify({"success": False})
    except Exception as e:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][currency]})
