import serial

# Set the port and baudrate in advance
SERIAL_PORT = "/dev/ttyACM0"
BAUDRATE = 9600


def open_serial_port():
    global ser
    try:
        ser = serial.Serial(SERIAL_PORT, BAUDRATE)
        ser.timeout = 2
        print("Connected to controller")
        return ser  # Opening succeeded
    except serial.SerialException:
        print("FAILED to connect!")
        return None  # Opening failed


def close_serial_port(ser):
    ser.flush()
    ser.timeout(1)
    ser.close()


def start_reference_run(ser):
    ser.write("G28".encode())
    #ser.timeout(1)
    while True:
        if ser.in_waiting:
            received_data = ser.read()#line().decode().strip()
            print(received_data)
            if received_data == "2k":
                return received_data
            elif received_data == "0k":
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
