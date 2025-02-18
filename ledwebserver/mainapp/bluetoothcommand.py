# serial_connection.py (or similar module)

import serial
import time
class BluetoothSerialConnection:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.connection = None

    def open(self):
        if not self.connection or not self.connection.is_open:
            try:
                self.connection = serial.Serial(self.port, self.baud_rate, timeout=1)
                print("Bluetooth serial connection established")
            except serial.SerialException as e:
                print(f"Failed to establish Bluetooth connection: {e}")

        else:
            print("Connection already open.")

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Serial connection closed.")

    def send(self, message):
        if self.connection and self.connection.is_open:
            message = message + '\n'
            self.connection.write(message.encode("utf-8"))
            print(message)
            #time.sleep(1)
            self.connection.flush()
        else:
            print("Connection is not open.")

    def receive(self):
        if self.connection and self.connection.is_open:
            return self.connection.readline().decode("utf-8").strip()
        return None


# Singleton instance
bluetooth_connection = BluetoothSerialConnection("/dev/cu.DSDTECHHC-05", 9600)
