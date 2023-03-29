import board
import busio
import displayio
import time

import adafruit_ili9341

import gui
import graphics
import dht

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
gui.refresh(TFT)
print(graphics.BLACK)

i = 3
while True:
    time.sleep(1)
    temperature = dht.get_temperature()
    humidity = dht.get_humidity()
    gui.update_temperature(temperature)
    gui.update_humidity(humidity)
    gui.refresh(TFT)
