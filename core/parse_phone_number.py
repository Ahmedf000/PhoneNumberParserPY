import phonenumbers
from phonenumbers import number_type
from parse_raw import CleanParser

raw = input('Enter a phone number to parse: ')
code = input('Enter a code: ').upper()
clean = CleanParser()
all_clean = [clean.leading,clean.internal,clean.leading_spaces, clean.dash]
raw_finalized  = raw
for func in all_clean:
        raw_finalized = func(raw_finalized)
print(raw_finalized)

class PhoneNumberParser:
    def __init__(self):
        self.parse = phonenumbers.parse(raw_finalized, code)
        self.valid = phonenumbers.is_valid_number(self.parse)
        self.phone_number = phonenumbers.format_number(self.parse, phonenumbers.PhoneNumberFormat.E164)
        self.type = phonenumbers.number_type(self.parse)

    def validate(self,):
        if self.valid:
            print("Phone Number is Valid")
            return (self.phone_number, self.type)
        else:
            print(f'Phone number {raw_finalized} is not valid')


