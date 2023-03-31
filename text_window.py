import displayio as dio

import gui
import graphics
import wifi_manager as wifi

from window import Window

class TextWindow(Window):

    def __init__(self) -> None:
        self.group = dio.Group(y=gui.main_window_height)
        self.text_label = graphics.make_label(2, -200, graphics.FONT_LUCIDA_GRANDE_12, "", graphics.COLOR_WHITE)

    def setup(self):
        self.group.append(self.text_label)
    
    def loop(self):
        networks = wifi.scan_nearby_networks()
        networks_text = ""
        for n in networks:
            networks_text = networks_text + f"\n{n}"
        self.append_text(networks_text)

    def deinit(self):
        del self.group
        del self.text_label

    def append_text(self, text):
        self.text_label.text += f"\n{text}"
        if self.text_label.height > gui.main_window_height:
            self.text_label.text = text