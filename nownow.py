import Adafruit_DHT
import requests
import time

# Define the sensor and the GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin where the sensor is connected

# Cloud service endpoint (replace with your endpoint)
CLOUD_ENDPOINT = "https://f3c3-2601-646-a000-7b40-00-902c.ngrok-free.app"

def read_sensor():
    """Read temperature and humidity from the DHT11 sensor."""
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f'Temperature={temperature}°C  Humidity={humidity}%')
        return {'temperature': temperature, 'humidity': humidity}
    else:
        print("Failed to retrieve data from sensor")
        return None

def send_to_cloud(data):
    """Send sensor data to the cloud endpoint."""
    try:
        response = requests.post(CLOUD_ENDPOINT, json=data)
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print(f"Failed to send data, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

def main():
    while True:
        sensor_data = read_sensor()
        if sensor_data:
            send_to_cloud(sensor_data)
        time.sleep(10)  # Adjust the interval as needed

if __name__ == "__main__":
    main()
