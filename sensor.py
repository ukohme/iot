import Adafruit_DHT
import requests
import time

# DHT11 sensor configuration
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Adjust to the GPIO pin you've connected the sensor to
CLOUD_ENDPOINT = "https://648b-73-231-28-149.ngrok-free.app"  # Local Flask server endpoint

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        data = {'temperature': temperature, 'humidity': humidity}
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        try:
            response = requests.post(CLOUD_ENDPOINT, json=data)
            if response.status_code == 200:
                print("Data sent successfully")
            else:
                print("Failed to send data")
        except requests.exceptions.RequestException as e:
            print(f"Error sending data: {e}")
    else:
        print("Failed to retrieve data from sensor")
    time.sleep(10)
