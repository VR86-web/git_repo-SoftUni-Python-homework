

from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class TestUserModel(TestCase):

    def test__valid_str_method(self):
        user = UserModel.objects.create_user(
            {
                'username': 'vlado',
                'email': 'vladi@vladi.com',
                'password': '12vlado34',
            }
        )

        self.assertEqual(str(user), user.email)