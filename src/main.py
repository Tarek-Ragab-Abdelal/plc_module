from helpers.httpClient import HttpClient
from helpers.serialClient import SerialClient
import config
import time

# Initialize clients
http_client = HttpClient(config.SERVER_URL, config.EMAIL, config.PASSWORD)
serial_client = SerialClient(config.PLC_IP, config.PLC_PORT)

def main():
    # Perform login
    if not http_client.token:
        print("Login failed. Exiting...")
        return
    
    # # Connect to PLC
    # if not serial_client.connect():
    #     print("Could not connect to PLC. Exiting...")
    #     return

    while True:
        # Read sensor data from PLC
        # sensor_value = serial_client.read_sensor(config.SENSOR_REGISTER, 1)
        sensor_value = 305
        if sensor_value is not None:
            print(f"Sensor Value: {sensor_value}")
            data = {
                'v': sensor_value,
                'bn': "temperature",
                'bv': 293,
                'n': "nozzle temperature",
                'u': "C",
                't': 1718889726,
                }
            # Format the endpoint with the sensor ID
            endpoint = config.TEPM_SENSOR_ENDPOINT.format(TEPM_SENSOR_ID=config.TEPM_SENSOR_ID)
            # Post sensor data to server
            http_client.post_data(endpoint, data)
        else:
            print(f"Not connected to PLC")

        # # Get LED control command from server
        # command = http_client.get_commands(config.COMMAND_ENDPOINT)
        # if command is not None and 'led_value' in command:
        #     led_value = command['led_value']
        #     # Control LED based on server command
        #     serial_client.control_led(config.LED_REGISTER, led_value)

        # Wait for a while before next cycle
        time.sleep(config.POLL_INTERVAL)

if __name__ == '__main__':
    main()
