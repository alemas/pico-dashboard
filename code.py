import board
import busio
import displayio
import time

import adafruit_ili9341

import gui
import graphics
import dht
import wifi_manager as wifi
import window_manager
from text_window import TextWindow

TFT_SCLK = board.GP2
TFT_RST = board.GP5

TFT_DC = board.GP6
TFT_MOSI = board.GP3
TFT_CS = board.GP8

displayio.release_displays()

SPI = busio.SPI(TFT_SCLK, TFT_MOSI)
DISPLAY_BUS = displayio.FourWire(SPI, command=TFT_DC, chip_select=TFT_CS, reset=TFT_RST)
TFT = adafruit_ili9341.ILI9341(DISPLAY_BUS, width=320, height=240)

gui.init()

wifi.stop_station()
wifi.connect(wifi.WIFI_SSID, wifi.WIFI_PASSWORD)

text_window = TextWindow()
window_manager.transition_to_window(text_window)

while True:
    gui.update_wifi()
    gui.update_temperature()
    gui.update_humidity()

    window_manager.window_loop()
    gui.draw(TFT)

    time.sleep(1)
