import unittest
from unittest.mock import patch, Mock
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from helpers.serialClient import SerialClient
import config as config

class TestSerialClient(unittest.TestCase):
    def setUp(self):
        self.serial_client = SerialClient(config.PLC_IP, config.PLC_PORT)

    @patch('pyModbusTCP.client.ModbusClient.open')
    def test_connect(self, mock_open):
        mock_open.return_value = True
        self.assertTrue(self.serial_client.connect())

        mock_open.return_value = False
        self.assertFalse(self.serial_client.connect())

    @patch('pyModbusTCP.client.ModbusClient.read_holding_registers')
    def test_read_sensor(self, mock_read_holding_registers):
        mock_read_holding_registers.return_value = [123]
        self.serial_client.connect()
        value = self.serial_client.read_sensor(config.SENSOR_REGISTER, 1)
        self.assertEqual(value, 123)

    @patch('pyModbusTCP.client.ModbusClient.write_single_register')
    def test_control_digital(self, mock_write_single_register):
        mock_write_single_register.return_value = True
        self.serial_client.connect()
        res
