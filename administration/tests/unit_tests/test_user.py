from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from administration.models import User


class UserTestCase(SimpleTestCase):
    def test_required_fields(self):
        user = User()

        with self.assertRaises(ValidationError) as e:
            user.full_clean()

        expected_message_dict = {
            'first_name': ['This field cannot be blank.'],
            'last_name': ['This field cannot be blank.'],
            'iban': ['This field cannot be blank.'],
            'created_by': ['This field cannot be null.'],
        }

        self.assertDictEqual(e.exception.message_dict, expected_message_dict)

    def test_first_name_max_length(self):
        user = User(first_name='a'*256)

        with self.assertRaises(ValidationError) as e:
            user.full_clean()

        expected_message_dict = [f'Ensure this value has at most 255 characters (it has {len(user.first_name)}).']

        self.assertEqual(e.exception.message_dict['first_name'], expected_message_dict)

    def test_last_name_max_length(self):
        user = User(last_name='a'*256)

        with self.assertRaises(ValidationError) as e:
            user.full_clean()

        expected_message_dict = [f'Ensure this value has at most 255 characters (it has {len(user.last_name)}).']

        self.assertEqual(e.exception.message_dict['last_name'], expected_message_dict)

    def test_iban_max_length(self):
        user = User(iban='TEST_IBAN')

        with self.assertRaises(ValidationError) as e:
            user.full_clean()

        expected_message_dict = [f'{user.iban} is not a valid IBAN.']

        self.assertEqual(e.exception.message_dict['iban'], expected_message_dict)
