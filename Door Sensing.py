import serial
import subprocess
import time

# Set up serial communication
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port
time.sleep(2)  # Allow time for the connection to establish

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        if data == "Door Opened":
            print("Door detected! Opening website...")
            subprocess.run(['start', 'chrome', '--new-window', 'https://mail.google.com/mail/u/0/#inbox'], shell=True)