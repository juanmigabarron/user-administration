import string

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Algorithm https://en.wikipedia.org/wiki/International_Bank_Account_Number#algorithms

COUNTRY_LENGTH = {
    'AL': 28, 'AD': 24, 'AT': 20, 'AZ': 28, 'BE': 16, 'BH': 22, 'BA': 20, 'BR': 29, 'BG': 22, 'CR': 21, 'HR': 21,
    'CY': 28, 'CZ': 24, 'DK': 18, 'DO': 28, 'EE': 20, 'FO': 18, 'FI': 18, 'FR': 27, 'GE': 22, 'DE': 22, 'GI': 23,
    'GR': 27, 'GL': 18, 'GT': 28, 'HU': 28, 'IS': 26, 'IE': 22, 'IL': 23, 'IT': 27, 'KZ': 20, 'KW': 30, 'LV': 21,
    'LB': 28, 'LI': 21, 'LT': 20, 'LU': 20, 'MK': 19, 'MT': 31, 'MR': 27, 'MU': 30, 'MC': 27, 'MD': 24, 'ME': 22,
    'NL': 18, 'NO': 15, 'PK': 24, 'PS': 29, 'PL': 28, 'PT': 25, 'RO': 24, 'SM': 27, 'SA': 24, 'RS': 22, 'SK': 24,
    'SI': 19, 'ES': 24, 'SE': 24, 'CH': 21, 'TN': 24, 'TR': 26, 'AE': 23, 'GB': 22, 'VG': 24
}

IBAN_CHARACTERS = string.digits + string.ascii_uppercase

# Representation of the Chars ('A' -> 65) and their representation in base36 (65 -> '10')
LETTERS_BASE36 = {ord(char): str(key) for key, char in enumerate(IBAN_CHARACTERS)}


def _country_length(iban):
    """ Checks if iban has the properly length of the country """
    country_code = iban[:2]
    country_length = COUNTRY_LENGTH.get(country_code)

    if country_length and country_code.isalpha() and len(iban) == country_length:
        return True

    return False


def _translate_iban(iban):
    """ Translates the iban in the correct format """
    return (iban[4:] + iban[:4]).translate(LETTERS_BASE36)


def validate_iban(value):
    """ Checks the country length and if the translated iban mod 97 is 1, otherwise raise an error """
    if not _country_length(value) or int(_translate_iban(value)) % 97 != 1:
        raise ValidationError(
            _(f'{value} is not a valid IBAN'),
            params={'value': value},
        )
