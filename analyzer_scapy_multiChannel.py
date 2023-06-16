import time
import random
import os
from threading import Thread
from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11ProbeResp, Dot11, RadioTap, Dot11Elt

access_points = {}
iface = "wlan0"  # Change this to your wireless interface name

def handle_packet(packet):
    if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()
        signal = packet[RadioTap].dBm_AntSignal
        try:
            channel = int(ord(packet[Dot11Elt:3].info))
        except:
            channel = None

        if bssid not in access_points:
            access_points[bssid] = (ssid, signal, channel)


def channel_hopper():
    while True:
        try:
            channel = random.randrange(1,14)  # Choose a random channel between 1 and 13
            os.system(f"iwconfig {iface} channel {channel}")  # Change to the chosen channel
            time.sleep(0.5)
        except KeyboardInterrupt:
            break

def scan_wifi():
    channel_thread = Thread(target=channel_hopper)
    channel_thread.daemon = True
    channel_thread.start()

    sniff(iface=iface, timeout=1, prn=handle_packet, store=False)
    return access_points

def choose_access_point(access_points):
    print("Available Wi-Fi Access Points:")
    for idx, (bssid, (ssid, signal, channel)) in enumerate(access_points.items()):
        print(f"{idx + 1}. SSID: {ssid}, BSSID: {bssid}, Signal: {signal} dBm, Channel: {channel}")

    selected_idx = int(input("\nEnter the index of the access point you want to track: "))
    bssid = list(access_points.keys())[selected_idx - 1]
    return bssid, access_points[bssid]

def track_signal_quality(bssid):
    while True:
        access_points.clear()
        scan_wifi()
        if bssid in access_points:
            print(f"Signal quality of {access_points[bssid][0]} (BSSID: {bssid}, Channel: {access_points[bssid][2]}): {access_points[bssid][1]} dBm")
        else:
            print(f"{bssid} not found")
        time.sleep(0.5)

if __name__ == "__main__":
    access_points = scan_wifi()
    selected_ap = choose_access_point(access_points)
    print(f"\nTracking signal quality of {selected_ap[1][0]} (BSSID: {selected_ap[0]})\n")
    track_signal_quality(selected_ap[0])