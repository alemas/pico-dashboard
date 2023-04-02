import displayio as dio
import adafruit_display_text as dt
import gc

import gui
import graphics
import wifi_manager as wifi
import network_manager as net

from window import Window

class TextWindow(Window):

    def __init__(self) -> None:
        self.group = dio.Group(y=gui.STATUS_BAR_HEIGHT)
        self.text_label = graphics.make_label(2, 8, graphics.FONT_LUCIDA_GRANDE_12, "", graphics.COLOR_WHITE)

        self.text = ""
        self.max_lines = int(gui.main_window_height / 20)
        self.lines_count = 0

    def setup(self):
        self.group.append(self.text_label)
    
    def loop(self):
        # networks = wifi.scan_nearby_networks()
        # networks_text = ""
        # for n in networks:
        #     networks_text = networks_text + f"\n{n}"
        # self.append_text(networks_text)

        self.text = net.get_quotes()
        print(len(self.text.encode('utf-8')))
        self.__set_text()
        del self.text
        gc.collect()

    def deinit(self):
        del self.group
        del self.text_label

    def __set_text(self):
        self.text = "\n".join(dt.wrap_text_to_pixels(self.text, 320, self.text_label.font))
        self.text_label.text = self.text