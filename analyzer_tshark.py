import subprocess
import time
from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11ProbeResp, Dot11, RadioTap, Dot11Elt

access_points = {}

def handle_output(output):
    lines = output.decode().split("\n")
    for line in lines:
        if "Beacon" in line or "Probe Response" in line:
            parts = line.split()
            bssid = parts[2]
            ssid = parts[3]
            signal = parts[4]
            if bssid not in access_points:
                access_points[bssid] = (ssid, signal)

def scan_wifi():
    command = ["tshark", "-i", "wlan0", "-Y", "wlan.fc.type_subtype eq 8 or wlan.fc.type_subtype eq 5", "-T", "fields", "-e", "wlan.sa", "-e", "wlan.ssid", "-e", "radiotap.dbm_antsignal"]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    handle_output(result.stdout)
    return access_points

def choose_access_point(access_points):
    print("Available Wi-Fi Access Points:")
    for idx, (bssid, (ssid, signal)) in enumerate(access_points.items()):
        print(f"{idx + 1}. SSID: {ssid}, BSSID: {bssid}, Signal: {signal} dBm")

    selected_idx = int(input("\nEnter the index of the access point you want to track: "))
    bssid = list(access_points.keys())[selected_idx - 1]
    return bssid, access_points[bssid]

def track_signal_quality(bssid):
    while True:
        access_points.clear()
        scan_wifi()
        if bssid in access_points:
            print(f"Signal quality of {access_points[bssid][0]} (BSSID: {bssid}): {access_points[bssid][1]} dBm")
        else:
            print(f"{bssid} not found")

if __name__ == "__main__":
    access_points = scan_wifi()
    selected_ap = choose_access_point(access_points)
    print(f"\nTracking signal quality of {selected_ap[1][0]} (BSSID: {selected_ap[0]})\n")
    track_signal_quality(selected_ap[0])
