import Adafruit_DHT
import requests
import time
import logging
from typing import Tuple, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
class Config:
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4  # GPIO pin where the sensor is connected
    CLOUD_ENDPOINT = "http://your-cloud-service.com/api/sensor-data"
    READ_INTERVAL = 10  # seconds
    RETRY_COUNT = 3
    RETRY_DELAY = 2  # seconds

def read_sensor_data() -> Tuple[Optional[float], Optional[float]]:
    """
    Read temperature and humidity from DHT11 sensor.
    Returns tuple of (humidity, temperature) or (None, None) if reading fails.
    """
    try:
        humidity, temperature = Adafruit_DHT.read_retry(
            Config.DHT_SENSOR, 
            Config.DHT_PIN,
            retries=Config.RETRY_COUNT,
            delay_seconds=Config.RETRY_DELAY
        )
        return humidity, temperature
    except Exception as e:
        logging.error(f"Error reading sensor: {e}")
        return None, None

def send_to_cloud(temperature: float, humidity: float) -> bool:
    """
    Send temperature and humidity data to cloud service.
    Returns True if successful, False otherwise.
    """
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': time.time()
    }
    
    try:
        response = requests.post(
            Config.CLOUD_ENDPOINT, 
            json=data,
            timeout=5  # 5 seconds timeout
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending data to cloud: {e}")
        return False

def main():
    logging.info("Starting DHT11 sensor monitoring...")
    
    while True:
        try:
            # Read sensor data
            humidity, temperature = read_sensor_data()
            
            if humidity is not None and temperature is not None:
                # Log the values
                logging.info(f'Temperature={temperature:.1f}°C  Humidity={humidity:.1f}%')
                
                # Send to cloud
                if send_to_cloud(temperature, humidity):
                    logging.info("Data sent successfully to cloud")
                else:
                    logging.warning("Failed to send data to cloud")
            else:
                logging.warning("Failed to retrieve data from sensor")
                
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            
        finally:
            # Wait before next reading
            time.sleep(Config.READ_INTERVAL)

if __name__ == "__main__":
    main()
