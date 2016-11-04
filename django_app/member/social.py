from urllib.request import urlopen

from django.core.files.base import ContentFile
from social.utils import slugify

USER_FIELDS = ['email', 'nickname']


def create_user(strategy, details, user=None, *args, **kwargs):
    print(details)
    print(kwargs)
    if user:
        return {'is_new': False}

    fields = {'email': details.get('email'), 'nickname': details.get('username'), 'first_name': details.get('first_name'), 'last_name': details.get('last_name'), 'phone_number': '00000000000'}

    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }
