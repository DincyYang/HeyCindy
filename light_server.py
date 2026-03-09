from flask import Flask

app = Flask(__name__)
light_on = False

@app.route("/")
def home():
    if light_on:
        return "<body style='background-color:yellow;'></body>"
    else:
        return "<body style='background-color:black;'></body>"

@app.route("/on")
def turn_on():
    global light_on
    light_on = True
    return "ON"

@app.route("/off")
def turn_off():
    global light_on
    light_on = False
    return "OFF"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)