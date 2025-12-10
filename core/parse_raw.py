import re


class CleanParser:
    def __init__(self):
        self.leading_zeros = re.compile(r'^0+')
        self.internal_zeros = re.compile(r'\(0+([^)]+)\)')
        self.leading_and_spaces = re.compile(r'^0+\s*')
        self.dashes = re.compile(r'-\s*')
        self.whitelist_pattern = re.compile(r'[^0-9\s\+\-\(\)]')

    def sanitize(self, text):
        if not text:
            return ""

        text = str(text)

        if len(text) > 100:
            text = text[:100]

        sanitized = self.whitelist_pattern.sub('', text)

        return sanitized

    def leading(self, text):
        if not text:
            return ""
        return self.leading_zeros.sub('', text)

    def internal(self, text):
        if not text:
            return ""
        return self.internal_zeros.sub(r'\1', text)

    def leading_spaces(self, text):
        if not text:
            return ""
        return self.leading_and_spaces.sub('', text)

    def dash(self, text):
        if not text:
            return ""
        return self.dashes.sub('', text)