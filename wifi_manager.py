import os
import ipaddress
import wifi

WIFI_SSID = os.getenv("WIFI_SSID")
WIFI_PASSWORD = os.getenv("WIFI_PASSWORD")
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

def scan_nearby_networks() -> list:
    networks = map(lambda x: x.ssid if len(x.ssid.strip()) > 0 else "No name", WIFI_RADIO.start_scanning_networks())
    set_networks = set(networks)
    WIFI_RADIO.stop_scanning_networks()
    return set_networks

def is_connected() -> bool:
    return not ip_address() is None

def is_online() -> bool:
    google_ipv4 = ipaddress.ip_address("8.8.8.8")
    ping = WIFI_RADIO.ping(google_ipv4)
    return not ping is None

def signal_strength() -> int:
    # if is_connected():
        # if not WIFI_RADIO.ap_info is None:
        #     return WIFI_RADIO.ap_info.rssi
    # As of now, CircuitPython 8.0.2 on a raspberry pi pico will raise a 'NotImplementeError' when calling 'ap_info'
    return None

def mac_address() -> str:
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

def ip_address() -> str:
    return f"{WIFI_RADIO.ipv4_address}"

