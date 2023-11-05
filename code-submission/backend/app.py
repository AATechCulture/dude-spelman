from flask import Flask, request, Response
import cancellation_prediction

app = Flask(__name__)


@app.route("predict-cancellation", methods=["GET"])
def predict_cancellation():
    data = request.get_json()
    if not data:
        return Response(status=400)

    flight_number = data["flight_number"]
    flight_date = data["flight_date"]
    result = cancellation_prediction.get_cancellation_percentage(
        flight_number, flight_date
    )

    return result


@app.route("/flight_info")
def get_flight_info():
    return "nothing"

if __name__ == "__main__":
    app.run(debug=True)
