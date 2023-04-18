import time
import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(3)

    bss_list = iface.scan_results()
    access_points = []

    for bss in bss_list:
        access_points.append((bss.ssid, bss.bssid, bss.signal))
    
    return access_points

def choose_access_point(access_points):
    print("Available Wi-Fi Access Points:")
    for idx, ap in enumerate(access_points):
        print(f"{idx + 1}. SSID: {ap[0]}, BSSID: {ap[1]}, Signal: {ap[2]} dBm")
    
    selected_idx = int(input("\nEnter the index of the access point you want to track: "))
    return access_points[selected_idx - 1]

def track_signal_quality(bssid):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    while True:
        iface.scan()
        time.sleep(2)

        bss_list = iface.scan_results()

        for bss in bss_list:
            if bss.bssid == bssid:
                print(f"Signal quality of {bssid}: {bss.signal} dBm")
                break

if __name__ == "__main__":
    access_points = scan_wifi()
    selected_ap = choose_access_point(access_points)
    print(f"\nTracking signal quality of {selected_ap[0]} (BSSID: {selected_ap[1]})\n")
    track_signal_quality(selected_ap[1])