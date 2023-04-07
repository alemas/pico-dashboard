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
        print(net.get_forecast(), "\n")
        pass

    def deinit(self):
        del self.group
        del self.text_label

    def __set_text(self):
        self.text = "\n".join(dt.wrap_text_to_pixels(self.text, 320, self.text_label.font))
        self.text_label.text = self.text