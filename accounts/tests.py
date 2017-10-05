import json
from urllib.parse import urlencode
from urllib.request import urlopen

from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings

from accounts.models import Profile
from accounts.functions import get_token


class AccountsTestCase(TestCase):
    def setUp(self):
        pass

    def test_new_user_gets_profile(self):
        """Profile should be created when a new user is created"""
        user = User.objects.create_user('test',
                                        'test@openstax.org',
                                        'testpassword')

        try:
            Profile.objects.get(user=user)
        except:
            self.fail("Account profile creation failed.")

    def test_accounts_contains_uuid(self):
        token = get_token()
        url = settings.USERS_QUERY + urlencode({
            'q': 'id:{}'.format("2"),
            'access_token': token['access_token']
        })

        with urlopen(url) as url:
            data = json.loads(url.read().decode())
            uuid = data['items'][0]['uuid']

        self.assertEqual(uuid, "aaa560a1-e828-48fb-b9a8-d01e9aec71d0")
