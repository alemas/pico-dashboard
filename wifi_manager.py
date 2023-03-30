import os
import ipaddress
import wifi
import socketpool

WIFI_SSID = ""
WIFI_PASSWORD = ""

WIFI_RADIO = wifi.radio

def connect(ssid, psswd) -> bool:
    try:
        WIFI_RADIO.connect(ssid, psswd)
        return True
    except:
        return False
    
def stop_station():
    WIFI_RADIO.stop_station()

def start_station():
    WIFI_RADIO.start_station()

def is_online() -> bool:
    google_ipv4 = ipaddress.ip_address("8.8.8.8")
    ping = WIFI_RADIO.ping(google_ipv4)
    return not ping is None

def signal_strength() -> int:
    WIFI_RADIO.rssi

def mac_address():
    if WIFI_RADIO.mac_address:
        mac = ""
        for index, value in enumerate(WIFI_RADIO.mac_address):
            component = f"{hex(value)}"[2:].upper()
            if len(component) == 1 :
                component = f"0{component}"
            mac = mac + ":" + component if index != 0 else component
        return mac
    else:
        return None

def ip_address():
    return f"{WIFI_RADIO.ipv4_address}"
