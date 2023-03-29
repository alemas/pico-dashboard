import adafruit_dht
import board

DHT_PIN = board.GP9

DHT = adafruit_dht.DHT11(DHT_PIN)

def get_temperature() -> float:
    temp = DHT.temperature
    if temp:
        return temp
    return 0

def get_humidity() -> float:
    hum = DHT.humidity
    if hum:
        return hum
    return 0

