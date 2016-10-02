# -*- coding: latin-1 -*-
import logging

class KeyLogger(object):
    """ Send user message """
    def __init__(self, **kwargs):
        self.word = kwargs.get('word', '')
        FORMAT = '%(asctime)-15s %(message)s'
        logging.basicConfig(filename='example.log', level=logging.DEBUG, format=FORMAT)

    def append_char(self, key):
        """ Append char to word """
        self.word += key.char if hasattr(key, 'char') else key

    def append_key(self, key):
        """ Append key to word """
        self.word += '<{0}>'.format(key.name)

    def send(self):
        """ Send word message """
        logging.debug(self.word)
        self.word = ''
