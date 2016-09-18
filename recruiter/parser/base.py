from bs4 import BeautifulSoup


class Base(object):
    dom = None
    text = None
    params = {}

    def __init__(self, text, params={}):
        self.dom = BeautifulSoup(text, 'html.parser')
        self.text = text
        self.params = params
