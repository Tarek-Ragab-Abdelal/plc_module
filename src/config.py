# PLC Configs
PLC_IP = '192.168.0.1'
PLC_PORT = 502
SENSOR_REGISTER = 0
LED_REGISTER = 1

# Backend Configs
SERVER_URL = 'http://localhost:4000/api'
EMAIL = 'tarek@example.com'
PASSWORD = '12345678'
TEPM_SENSOR_ID = '66757c879087f55851cfe033'
COMMAND_ENDPOINT = 'api/led_command'
LOGIN_ENDPOINT = 'users/login'
TEPM_SENSOR_ENDPOINT = 'sensorReadings/{TEPM_SENSOR_ID}'


# General
POLL_INTERVAL = 5  # Polling interval in seconds
