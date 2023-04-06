import gui
import gc

from window import Window

CURRENT_WINDOW = None

def transition_to_window(window: Window):
    gui.set_main_window(window)
    global CURRENT_WINDOW
    if CURRENT_WINDOW:
        CURRENT_WINDOW.deinit()
        CURRENT_WINDOW = None
        gc.collect()
    window.setup()
    CURRENT_WINDOW = window

def window_loop():
    if CURRENT_WINDOW:
        CURRENT_WINDOW.loop()
        gc.collect()