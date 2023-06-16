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
        essids = ['ESSID1', 'ESSID2', 'ESSID3']

        essid_dropdown = tk.OptionMenu(self, self.selected_essid, *essids)
        essid_dropdown.config(bg="Grey", width=25)
        essid_dropdown.place(x=200, y=200)

# Send chosen ESSID
    def send_ssid(self):
        ssid = self.selected_essid.get()
        print(ssid)

    # def scan_wifi_networks(self):
    #     # Airport command to scan for Wi-Fi networks
    #     airport_cmd = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport","-s"]
    #
    #     # Scan Wi-Fi networks and parse the ESSIDs
    #     scan_output = subprocess.check_output(airport_cmd).decode("utf-8")
    #     essids = [line.split()[0] for line in scan_output.splitlines()[1:]]
    #
    #     essid_dropdown = tk.OptionMenu(self, self.selected_essid, *essids)
    #     essid_dropdown.config(bg="Grey")
    #     essid_dropdown.place(x=220, y=200)

    # def scan_wifi_networks(self):
    #     # Command to scan for Wi-Fi networks using netsh on Windows
    #     netsh_cmd = ['netsh', 'wlan', 'show', 'network', 'mode=Bssid']
    #
    #     # Scan Wi-Fi networks and parse the SSIDs
    #     scan_output = subprocess.check_output(netsh_cmd).decode('latin-1')
    #     ssids = re.findall(r'SSID\s+\d+\s+:\s+(.*)', scan_output)
    #
    #     essid_dropdown = tk.OptionMenu(self, self.selected_essid, *ssids)
    #     essid_dropdown.config(bg="Grey")
    #     essid_dropdown.place(x=220, y=200)

    # def scan_wifi_networks(self):
    #     # Command to scan for Wi-Fi networks using iwlist on Linux
    #     iwlist_cmd = ['iwlist', 'wlan0', 'scan']
    #
    #     # Scan Wi-Fi networks and parse the SSIDs
    #     scan_output = subprocess.check_output(iwlist_cmd).decode('utf-8')
    #     ssids = re.findall(r'ESSID:"(.*?)"', scan_output)
    #
    #     essid_dropdown = tk.OptionMenu(self, self.selected_essid, *ssids)
    #     essid_dropdown.config(bg="Grey")
    #     essid_dropdown.place(x=220, y=200)

    # def scan_wifi_networks(self):
    #     # Scapy command to scan for Wi-Fi networks
    #     wifi_networks = []
    #     for channel in range(1, 14):
    #         wifi_packets = sniff(iface='enp0s3', timeout=5, count=20, prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\n%Dot11Beacon.info%}"))
    #         for packet in wifi_packets:
    #             if packet.haslayer(Dot11Beacon):
    #                 ssid = packet[Dot11Elt].info.decode()
    #                 if ssid not in wifi_networks:
    #                     wifi_networks.append(ssid)
    #
    #     essid_dropdown = tk.OptionMenu(self, self.selected_essid, *wifi_networks, value=wifi_networks[0])
    #     essid_dropdown.config(bg="Grey")
    #     essid_dropdown.place(x=220, y=200)
