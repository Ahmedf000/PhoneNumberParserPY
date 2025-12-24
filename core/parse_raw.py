import re

class CleanParser:
    def __init__(self):
        self.leading_zeros = re.compile(r'^0+\s*')
        self.internal_zeros = re.compile(r'\(0+([^)]+)\)')
        self.dashes = re.compile(r'-\s*')
        self.commas = re.compile(r',')

    def leading(self, text):
        return self.leading_zeros.sub('', text)

    def internal(self, text):
        return self.internal_zeros.sub(r'\1', text)

    def dash(self, text):
        return self.dashes.sub('', text)

    def comma(self, text):
        return self.commas.sub('', text)