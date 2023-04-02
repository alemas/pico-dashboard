import gui
import gc

from window import Window

CURRENT_WINDOW = None

def transition_to_window(window: Window):
    print(f'Free memory before transition: {gc.mem_free()}B')
    gui.set_main_window(window)
    global CURRENT_WINDOW
    if CURRENT_WINDOW:
        CURRENT_WINDOW.deinit()
        CURRENT_WINDOW = None
        gc.collect()
    window.setup()
    CURRENT_WINDOW = window
    print(f'Free memory after transition: {gc.mem_free()}B\n')

def window_loop():
    if CURRENT_WINDOW:
        CURRENT_WINDOW.loop()
        gc.collect()