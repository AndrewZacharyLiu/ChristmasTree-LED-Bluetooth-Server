from django.apps import AppConfig
import serial
import time
from django.conf import settings
from django.db.backends.signals import connection_created
from django.db import connections
import atexit
from .bluetoothcommand import *
class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

    
    def ready(self):
        # Open the Bluetooth serial connection at startup
        bluetooth_connection.open()

        # Optionally, add a handler to close the connection when the server stops
        atexit.register(self.close_connection)

    def close_connection(self):
        # Close the serial connection when the server stops
        bluetooth_connection.close()

