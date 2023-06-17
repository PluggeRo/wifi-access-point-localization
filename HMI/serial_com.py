import serial

# Set the port and baudrate in advance
SERIAL_PORT = "/dev/ttyACM0"
BAUDRATE = 9600

ser = None


def open_serial_port():
    global ser
    try:
        ser = serial.Serial(SERIAL_PORT, BAUDRATE)
        ser.timeout = 2
        print("Connected to controller")
        return True  # Opening succeeded
    except serial.SerialException:
        print("FAILED to connect!")
        return False  # Opening failed


def close_serial_port(ser):
    ser.flush()
    ser.timeout(1)
    ser.close()


def start_reference_run(ser):
    ser.write("G28 \n".encode())
    ser.timeout(1)
    while True:
        if ser.in_waiting:
            received_data = ser.readline().decode().strip()
            if received_data == "2":
                return received_data
            elif received_data == "0":
                print("Reference run failed")
                return received_data


def pointer_vertical_degree(degree):
    ser.write(f"G11 {degree} \n".encode())
    ser.timeout(1)
    while True:
        if ser.in_waiting:
            received_data = ser.readline().decode().strip()
            if received_data == "2":
                return received_data
            elif received_data == "0":
                print("Positioning failed")
                return received_data


def pointer_vertical_coordinates(coordinate):
    ser.write(f"G12 {coordinate} \n".encode())
    ser.timeout(1)
    while True:
        if ser.in_waiting:
            received_data = ser.readline().decode().strip()
            if received_data == "2":
                return received_data
            elif received_data == "0":
                print("Positioning failed")
                return received_data


def pointer_horizontal_degree(degree):
    ser.write(f"G21 {degree} \n".encode())
    ser.timeout(1)
    while True:
        if ser.in_waiting:
            received_data = ser.readline().decode().strip()
            if received_data == "2":
                return received_data
            elif received_data == "0":
                print("Positioning failed")
                return received_data


def pointer_horizontal_coordinates(coordinate):
    ser.write(f"G22 {coordinate} \n".encode())
    ser.timeout(1)
    while True:
        if ser.in_waiting:
            received_data = ser.readline().decode().strip()
            if received_data == "2":
                return received_data
            elif received_data == "0":
                print("Positioning failed")
                return received_data
