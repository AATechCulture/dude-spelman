from flask import Flask, request, Response, jsonify
import cancellation_prediction
import flight_info

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


@app.route("/flight_info", methods=['GET'])
def get_flight_info():
    
    data = request.get_json()
    if not data:
        return Response(status=400)
    
    originLocationCode = data["origin_location_code"]
    destinationLocationCode = data["destination_location_code"]
    departureDate = data["departure_date"]
    adults = data["adults"]
    
    return jsonify(flight_info.get_flight_info(originLocationCode, destinationLocationCode, departureDate, adults))

if __name__ == "__main__":
    app.run(debug=True)
