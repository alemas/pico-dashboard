import displayio as dio
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.rect import Rect

import graphics
import dht
import wifi_manager as wifi
from window import Window

# ----- HELPER METHODS

def set_group_item(group: dio.Group, item, index: int):
    items_count = len(group)
    if index >= 0 and index < items_count:
        group[index] = item
    else:
        group.append(item)

# ----- DRAWING METHODS

# display = None
ROOT_GROUP = dio.Group()
WINDOW_GROUP = dio.Group()

def init():
    set_group_item(ROOT_GROUP, WINDOW_GROUP, 0)
    set_group_item(ROOT_GROUP, Rect(0, 0, 320, STATUS_BAR_HEIGHT, fill=status_bar_background_color), 1)
    set_group_item(ROOT_GROUP, Line(0, STATUS_BAR_HEIGHT, 320, STATUS_BAR_HEIGHT, graphics.COLOR_WHITE), 2)

    __init_wifi()
    __init_temperature()
    __init_humidity()
    __init_time()

# STATUS BAR

status_bar_background_color = graphics.COLOR_BLACK
STATUS_BAR_HEIGHT = 32
STATUS_BAR_H_PADDING = 5

WIFI_GROUP = dio.Group()

TEMP_LABEL = None
HUMIDITY_LABEL = None
TIME_LABEL = None

def draw(display):
    display.show(ROOT_GROUP)

def __init_wifi():
    WIFI_GROUP.x = 283
    WIFI_GROUP.y = 2

    update_wifi()

    set_group_item(ROOT_GROUP, WIFI_GROUP, 3)

def __init_temperature():
    x = 175
    temp_image_group = dio.Group()
    temp_image_group.x = x
    temp_image_group.y = 2

    temp_image = graphics.make_image('temperature')
    set_group_item(temp_image_group, temp_image, 0)

    global TEMP_LABEL
    TEMP_LABEL = graphics.make_label(x+20, int(STATUS_BAR_HEIGHT/2), graphics.FONT_LUCIDA_GRANDE_12, "", graphics.COLOR_WHITE)
    set_group_item(ROOT_GROUP, temp_image_group, 4)
    set_group_item(ROOT_GROUP, TEMP_LABEL, 5)

def __init_humidity():
    x = 230
    humidity_image_group = dio.Group()
    humidity_image_group.x = x
    humidity_image_group.y = 5

    humidity_image = graphics.make_image('humidity')
    set_group_item(humidity_image_group, humidity_image, 0)

    global HUMIDITY_LABEL
    HUMIDITY_LABEL = graphics.make_label(x+20, int(STATUS_BAR_HEIGHT/2), graphics.FONT_LUCIDA_GRANDE_12, "", graphics.COLOR_WHITE)
    set_group_item(ROOT_GROUP, humidity_image_group, 6)
    set_group_item(ROOT_GROUP, HUMIDITY_LABEL, 7)

def __init_time():
    global TIME_LABEL
    TIME_LABEL = graphics.make_label(STATUS_BAR_H_PADDING, int(STATUS_BAR_HEIGHT/2), graphics.FONT_LUCIDA_GRANDE_BOLD_16, '09:41 Wed 13 Mar', graphics.COLOR_WHITE)
    set_group_item(ROOT_GROUP, TIME_LABEL, 8)

def __update_wifi(status):
    wifi_image = None

    # Connected, full signal
    if status == 0:
        wifi_image = graphics.make_image('wifi_full')
    # Connected, medium signal
    elif status == 1:
        wifi_image = graphics.make_image('wifi_med')
    # Connected, low signal
    elif status == 2:
        wifi_image = graphics.make_image('wifi_low')
    # Connecting
    elif status == 3:
        wifi_image = graphics.make_image('wifi_connecting')
    # Connected, offline
    elif status == 4:
        wifi_image = graphics.make_image('wifi_offline')
    # Not connected
    else:
        wifi_image = graphics.make_image('no_wifi')

    WIFI_GROUP.x = 320 - wifi_image.tile_width - STATUS_BAR_H_PADDING
    WIFI_GROUP.y = 2

    set_group_item(WIFI_GROUP, wifi_image, 0)

def update_wifi():
    if not wifi.is_connected():
        __update_wifi(5)
    elif not wifi.is_online():
        __update_wifi(4)
    else:
        __update_wifi(0)

def update_temperature():
    temperature = dht.get_temperature()
    TEMP_LABEL.text = str(temperature) + "°C"

def update_humidity():
    humidity = dht.get_humidity()
    HUMIDITY_LABEL.text = str(humidity) + "%"

# MAIN WINDOW

MAIN_WINDOW = None
main_window_height = 240 - STATUS_BAR_HEIGHT

def set_main_window(window: Window):
    global MAIN_WINDOW
    global WINDOW_GROUP
    MAIN_WINDOW = window
    WINDOW_GROUP = window.group
    set_group_item(ROOT_GROUP, WINDOW_GROUP, 0)
