from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def test():
    return "hi"

@app.route("/flight_info")
def get_flight_info():
    return "nothing"

if __name__ == "__main__":
    app.run(debug=True)