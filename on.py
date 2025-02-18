import serial

# Replace this with the actual virtual serial port assigned to your HC-05 on your system
# On macOS, it typically looks like /dev/cu.HC-05-DevB or similar
serial_port = "/dev/cu.DSDTECHHC-05"  # Replace with your HC-05 serial port
baud_rate = 9600  # Default baud rate for HC-05

# Establish serial connection to HC-05
try:
    hc05 = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to HC-05 on {serial_port}")

    while True:
        message = input("Enter message: ")
        message = message + '\n'  # Ensure newline to indicate message end
        hc05.write(message.encode("utf-8"))  # Send the message to HC-05
        print(f"Sent: {message}")
        response = ""
        while hc05.in_waiting > 0:
            response += hc05.readline().decode('utf-8').strip()  # Read each line of response

        if response:
            print(f"Received: {response}")
        else:
            print("No response received.")

except serial.SerialException as e:
    print(f"Error connecting to {serial_port}: {e}")

except KeyboardInterrupt:
    print("\nConnection closed.")

finally:
    if 'hc05' in locals() and hc05.is_open:
        hc05.close()
        print("Serial connection closed.")
