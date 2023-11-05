from flask import Flask, request, Response, jsonify
import cancellation_prediction
import flight_info
import weather_data
import flight_engine
import dateutil

app = Flask(__name__)


@app.route("/predict-cancellation", methods=["GET"])
def predict_cancellation():
    if "flight_number" not in request.args or "flight_date" not in request.args:
        return Response(status=400)

    flight_number = request.args["flight_number"]
    flight_date = request.args["flight_date"]
    result = cancellation_prediction.get_cancellation_percentage(
        flight_number, flight_date
    )

    return result


@app.route("/get-weather", methods=["GET"])
def get_weather():
    if "flight_number" not in request.args or "flight_date" not in request.args:
        return Response(status=400)

    flight_number = request.args["flight_number"]
    flight_date = request.args["flight_date"]

    flight_info = flight_engine.find_flight_info(flight_number, flight_date)
    airport_info = flight_engine.get_airport_info(flight_info["origin"]["code"])

    long, lat = (
        airport_info["location"]["longitude"],
        airport_info["location"]["latitude"],
    )
    result = weather_data.get_weather_data(
        long, lat, flight_info["departureTime"]
    )

    return result  # JSON


@app.route("/flight_info", methods=["GET"])
def get_flight_info():
    if not request.args:
        return Response(status=400)

    originLocationCode = request.args["origin_location_code"]
    destinationLocationCode = request.args["destination_location_code"]
    departureDate = request.args["departure_date"]
    adults = request.args["adults"]

    return jsonify(
        flight_info.get_flight_info(
            originLocationCode, destinationLocationCode, departureDate, adults
        )
    )


if __name__ == "__main__":
    app.run(port=8000, debug=True)
