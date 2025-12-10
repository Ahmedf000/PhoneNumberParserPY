import phonenumbers
from phonenumbers import NumberParseException
from core.parse_raw import CleanParser

TYPE_NAMES = {
    0: "FIXED-LINE",
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
    -1: "UNKNOWN",
}


class PhoneNumberParser:
    def __init__(self, raw, code):
        self.raw_original = raw
        self.raw_finalized = ""
        self.parse = None
        self.valid = False
        self.phone_number = None
        self.type = -1
        self.error_message = None

        if raw is None:
            self.error_message = "Error: No phone number provided (None)"
            return

        if not str(raw).strip():
            self.error_message = "Error: Phone number cannot be empty"
            return

        clean = CleanParser()
        raw_sanitized = clean.sanitize(raw)

        if not raw_sanitized.strip():
            self.error_message = "Error: No valid phone number characters found"
            return

        all_clean = [
            clean.leading,
            clean.internal,
            clean.leading_spaces,
            clean.dash
        ]

        raw_finalized = raw_sanitized
        for func in all_clean:
            raw_finalized = func(raw_finalized)

        self.raw_finalized = raw_finalized

        if not raw_finalized.strip():
            self.error_message = "Error: Phone number is empty after cleaning"
            return

        try:
            self.parse = phonenumbers.parse(raw_finalized, code)
            self.valid = phonenumbers.is_valid_number(self.parse)

            if self.valid:
                self.phone_number = phonenumbers.format_number(
                    self.parse,
                    phonenumbers.PhoneNumberFormat.E164
                )
                self.type = phonenumbers.number_type(self.parse)
            else:
                self.error_message = f"Phone number '{raw_finalized}' is not valid for country code '{code}'"

        except NumberParseException as e:
            self.valid = False
            error_type = e.error_type

            if error_type == NumberParseException.INVALID_COUNTRY_CODE:
                self.error_message = f"Error: Invalid country code '{code}'"
            elif error_type == NumberParseException.NOT_A_NUMBER:
                self.error_message = f"Error: '{raw_finalized}' is not a valid phone number format"
            elif error_type == NumberParseException.TOO_SHORT_NSN:
                self.error_message = f"Error: Phone number '{raw_finalized}' is too short"
            elif error_type == NumberParseException.TOO_LONG:
                self.error_message = f"Error: Phone number '{raw_finalized}' is too long"
            else:
                self.error_message = f"Error: Unable to parse phone number - {str(e)}"

        except Exception as e:
            self.valid = False
            self.error_message = f"Unexpected error: {str(e)}"

    def validate(self):
        if self.valid and self.phone_number:
            return (self.phone_number, TYPE_NAMES.get(self.type, "UNKNOWN"))
        else:
            return self.error_message or "Error: Phone number validation failed"