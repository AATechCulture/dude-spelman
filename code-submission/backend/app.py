from flask import Flask, request, jsonify
import flight_info

app = Flask(__name__)

@app.route("/hello")
def test():
    return "hi"

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