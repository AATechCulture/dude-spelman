from flask import Flask, request, Response, jsonfiy
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


@app.route("/flight_info", methods=['POST'])
def get_flight_info():
    
    data = request.json
    originLocationCode = data.get('param1')
    destinationLocationCode = data.get('param2')
    departureDate = data.get('param3')
    adults = data.get('param4')
    
    return jsonify(flight_info.get_flight_info(originLocationCode, destinationLocationCode, departureDate, adults))

if __name__ == "__main__":
    app.run(debug=True)
