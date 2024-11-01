from flask import Flask, request, jsonify

app = Flask(__name__)
sensor_data = []

@app.route("/api/sensor-data", methods=["POST"])
def receive_sensor_data():
    data = request.json
    if 'temperature' in data and 'humidity' in data:
        sensor_data.append(data)
        print(f"Received data: {data}")
        return jsonify({"status": "success"}), 200
    return jsonify({"error": "Invalid data format"}), 400

@app.route("/view-data", methods=["GET"])
def view_data():
    return jsonify(sensor_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
