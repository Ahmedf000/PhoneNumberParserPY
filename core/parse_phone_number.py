import phonenumbers
from phonenumbers import number_type
from core.parse_raw import CleanParser
from phonenumbers import PhoneNumberType

TYPE_NAMES = {
    0: "FIXED_LINE",
    1: "MOBILE",
    2: "FIXED_LINE_OR_MOBILE",
    3: "TOLL_FREE",
    4: "PREMIUM_RATE",
    5: "SHARED_COST",
    6: "VOIP",
    7: "PERSONAL_NUMBER",
    8: "PAGER",
    9: "UAN",
    10: "VOICEMAIL",
    -1: "UNKNOWN"
}


class PhoneNumberParser:
    def __init__(self, raw, code):
        clean = CleanParser()
        all_clean = [clean.leading, clean.internal, clean.dash, clean.comma]
        raw_finalized = raw
        for func in all_clean:
            raw_finalized = func(raw_finalized)

        self.raw_finalized = raw_finalized
        self.code = code
        self.parse = None
        self.valid = False
        self.phone_number = None
        self.type = -1
        self.error = None

        try:
            self.parse = phonenumbers.parse(raw_finalized, code)
            self.valid = phonenumbers.is_valid_number(self.parse)
            self.phone_number = phonenumbers.format_number(self.parse, phonenumbers.PhoneNumberFormat.E164)
            self.type = phonenumbers.number_type(self.parse)
        except phonenumbers.NumberParseException as e:
            self.error = str(e)
        except Exception as e:
            self.error = f"Unexpected error: {str(e)}"

    def validate(self):
        if self.error:
            return f"✗ Parse Error\n\n{self.error}"

        if self.valid:
            type_name = TYPE_NAMES.get(self.type, 'UNKNOWN')
            return f"✓ Valid Number\n\nFormatted: {self.phone_number}\nType: {type_name}"
        else:
            return f"✗ Invalid Number\n\n'{self.raw_finalized}' is not a valid phone number for country code '{self.code}'"
