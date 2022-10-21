from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/led/on")
def led_on():
    return "LED_ON"


@app.route("/led/off")
def led_off():
    return "LED_OFF"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
