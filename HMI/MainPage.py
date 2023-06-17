import tkinter as tk
from tkinter import ttk
import subprocess
import re
from scapy.all import *


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bg_image = tk.PhotoImage(file="Background.png")
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        button1 = tk.Button(self, text="Servo-control", command=lambda: controller.show_frame("PageTwo"))
        button1.place(x=10, y=425)

        self.selected_essid = tk.StringVar(self)
        self.selected_essid.set("Select ESSID")

        # Update to refresh the list of wifi-networks
        update_button = tk.Button(self, text="Update", command=self.scan_wifi_networks)
        update_button.place(x=390, y=425)

        # Button to send the chosen ESSID to analysis
        send_button = tk.Button(self, text="Send ESSID", command=self.send_ssid)
        send_button.place(x=450, y=200)

        # Button to exit GUI, due to fullscreen
        exit_button = tk.Button(self, text="Exit", width=8, command=controller.destroy)
        exit_button.place(x=700, y=425)

        self.scan_wifi_networks()

    def scan_wifi_networks(self):
        # Scan Wi-Fi networks and parse the ESSIDs
        essids = ["ESSID1", "ESSID2", "ESSID3"]

        essid_dropdown = tk.OptionMenu(self, self.selected_essid, *essids)
        essid_dropdown.config(bg="Grey", width=25)
        essid_dropdown.place(x=200, y=200)

# Send chosen ESSID
    def send_ssid(self):
        ssid = self.selected_essid.get()
        print(ssid)

