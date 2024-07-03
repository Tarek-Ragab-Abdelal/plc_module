from pyModbusTCP.client import ModbusClient

class SerialClient:
    def __init__(self, plc_ip, plc_port):
        self.client = ModbusClient(host=plc_ip, port=plc_port, auto_open=False)  # Set auto_open to False

    def connect(self):
        try:
            if self.client.open():
                print("Connected to PLC successfully.")
                return True
            else:
                print("Failed to connect to PLC.")
                return False
        except Exception as e:
            print(f"Exception during PLC connection: {e}")
            return False

    def read_sensor(self, register, num_registers):
        if self.client.is_open():
            sensor_values = self.client.read_holding_registers(register, num_registers)
            if sensor_values:
                return sensor_values[0]
            else:
                print("Failed to read sensor data.")
                return None
        else:
            print("PLC connection is not open.")
            return None

    def control_digital(self, register, value):
        if self.client.is_open():
            is_written = self.client.write_single_register(register, value)
            if is_written:
                print("LED state changed.")
                return True
            else:
                print("Failed to write to LED register.")
                return False
        else:
            print("PLC connection is not open.")
            return False
