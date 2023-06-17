import time
import tkinter as tk
import serial_com as sercom


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.angle_label = None
        self.angle_scale = None
        self.ser = None
        self.controller = controller

        # Set Background
        self.bg_image = tk.PhotoImage(file="Background.png")
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Button to switch between Main- and Control-Page
        main_button = tk.Button(self, text="Main", command=lambda: controller.show_frame("PageOne"))
        main_button.place(x=10, y=425)

        # Show the current Angle here
        angle = "-"
        angle_label = tk.Label(self, text=f"Current angle: {angle}")
        angle_label.config(bg="Grey")
        angle_label.place(x=300, y=100)

        # Scale to choose a position from 0 to 360
        angle_scale = tk.Scale(self, from_=0, to=360, orient=tk.HORIZONTAL, length=200)
        angle_scale.place(x=100, y=225)

        # Button to execute the movement
        move_button = tk.Button(self, text="Move Servo", command=sercom.open_serial_port)
        move_button.place(x=100, y=275)

        # Button to move the pointer up
        pointer_up_button = tk.Button(self, width=10, text="UP", command=self.up_to_serial)
        pointer_up_button.place(x=500, y=200)

        # Button to move the pointer down
        pointer_down_button = tk.Button(self, width=10, text="DOWN", command=self.down_to_serial)
        pointer_down_button.place(x=500, y=250)

        # Button to turn Radar to the left
        radar_left_button = tk.Button(self, width=10, text="LEFT", command=self.left_to_serial)
        radar_left_button.place(x=380, y=225)

        # Button to turn Radar to the right
        radar_right_button = tk.Button(self, width=10, text="RIGHT", command=self.right_to_serial)
        radar_right_button.place(x=620, y=225)

        # Step width Slider
        step_width_slider = tk.Scale(self, from_=1, to=30, orient=tk.VERTICAL, length=150)
        step_width_slider.place(x=750, y=150)

        # Button to start reference run
        reference_start_button = tk.Button(self, width=15, text="Reference run", command=self.start_ref_get_angle)
        reference_start_button.place(x=10, y=5)

    def up_to_serial(self):
        # Combine button touch with step-width
        read_angle = self.angle_scale # Read chosen angle from scale
        sercom.pointer_vertical_degree(+self.angle_scale)
        start_time = time.time()  # Get actual time
        return_value = None
        while return_value not in [2, 0]:
            if time.time() - start_time > 30:  # Check if 30 sec are passed
                print("Timeout reached. Exiting loop.")
                break
            return_value = sercom.pointer_vertical_degree
            if return_value == "2":
                angle = self.angle
                self.angle_label = tk.Label(self, text=f"Current angle: {read_angle}") # Apply angle to label
            elif return_value == 0:
                print("Movement failed!")
            else:
                print("Waiting for return...")
                time.sleep(5)

    def down_to_serial(self):
        # Combine button touch with step-width
        read_angle = -self.angle_scale  # Read chosen angle from scale
        sercom.pointer_vertical_degree(-self.angle_scale)
        start_time = time.time()  # Get actual time
        return_value = None
        while return_value not in [2, 0]:
            if time.time() - start_time > 30:  # Check if 30 sec are passed
                print("Timeout reached. Exiting loop.")
                break
            return_value = sercom.pointer_vertical_degree
            if return_value == "2":
                self.angle_label = tk.Label(self, text=f"Current angle: {read_angle}")  # Apply angle to label
            elif return_value == 0:
                print("Movement failed!")
            else:
                print("Waiting for return...")
                time.sleep(5)

    def left_to_serial(self):
        # Combine button touch with step-width
        sercom.pointer_horizontal_degree(-self.angle_scale)

    def right_to_serial(self):
        # Combine button touch with step-width
        sercom.pointer_horizontal_degree(+self.angle_scale)

    def start_ref_get_angle(self):
        # Save current angle to var
        sercom.open_serial_port() # Open serial connection
        time.sleep(2)
        start_time = time.time()  # Get actual time
        return_value = None
        while return_value not in [2, 0]:
            if time.time() - start_time > 30:  # Check if 30 sec are passed
                print("Timeout reached. Exiting loop.")
                break
            return_value = sercom.start_reference_run()
            if return_value == "2":
                angle = "0"
                self.angle_label = tk.Label(self, text=f"Current angle: {angle}")
            elif return_value == 0:
                print("Reference run failed!")
            else:
                print("Waiting for return...")
                time.sleep(5)
