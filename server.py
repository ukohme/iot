from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for data (alternatively, use a database for persistent storage)
sensor_data = []

@app.route("/api/sensor-data", methods=["POST"])
def receive_sensor_data():
    data = request.json
    if 'temperature' in data and 'humidity' in data:
        sensor_data.append(data)  # Store received data
        print(f"Received data: {data}")
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"error": "Invalid data format"}), 400

@app.route("/view-data", methods=["GET"])
def view_data():
    return jsonify(sensor_data), 200

if __name__ == "__main__":
    app.run(port=5000)
