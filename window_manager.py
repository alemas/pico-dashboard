import gui
from window import Window

CURRENT_WINDOW = None

def transition_to_window(window: Window):
    global CURRENT_WINDOW
    if CURRENT_WINDOW:
        CURRENT_WINDOW.deinit()
    window.setup()
    CURRENT_WINDOW = window
    gui.set_main_window(CURRENT_WINDOW)

def window_loop():
    if CURRENT_WINDOW:
        CURRENT_WINDOW.loop()