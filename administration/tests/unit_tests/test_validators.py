from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from administration.validators import _country_length, _translate_iban, validate_iban


class ValidatorsTestCase(SimpleTestCase):

    def test_country_length_ok(self):
        result = _country_length('ES1234567898765432123456')

        self.assertTrue(result)

    def test_country_length_error(self):
        result = _country_length('ES123456789876543212345')

        self.assertFalse(result)

    def test_translate_iban(self):

        expected_result = '14151610111213'

        result = _translate_iban('ABCDEFG')

        self.assertEqual(expected_result, result)

    def test_validate_iban_ok(self):
        self.assertIsNone(validate_iban('ES7921000813610123456789'))

    def test_validate_iban_error(self):
        iban = 'ES1234567898765432123456'

        with self.assertRaises(ValidationError) as e:
            validate_iban(iban)

        self.assertEqual(e.exception.message, f'{iban} is not a valid IBAN.')
