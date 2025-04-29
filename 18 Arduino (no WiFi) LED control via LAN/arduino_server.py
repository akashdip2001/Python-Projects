from flask import Flask, request
import serial
import time

# Adjust the serial port below (e.g., COM3 for Windows or /dev/ttyUSB0 for Linux)
SERIAL_PORT = 'COM9'  # <-- CHANGE THIS!
BAUD_RATE = 9600

# Initialize serial connection
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)  # wait for Arduino to reset

app = Flask(__name__)

@app.route('/led/<state>', methods=['GET'])
def control_led(state):
    if state == 'on':
        arduino.write(b'1')
        return 'LED turned ON'
    elif state == 'off':
        arduino.write(b'0')
        return 'LED turned OFF'
    else:
        return 'Invalid command', 400

if __name__ == '__main__':
    # Get IP address of your laptop and run the server
    app.run(host='0.0.0.0', port=5000)
    # Note: You can access the server using http://<your_ip>:5000/led/on or http://<your_ip>:5000/led/off