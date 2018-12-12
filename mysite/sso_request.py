from hashlib import sha256
from urllib.parse import urlencode

import requests

# Default config is for Example API ORG on web-stage.voxy.com
CONFIG = {
    'API_KEY': '4ctILLZk3tSNXXlf',
    'API_SECRET': 'FlmmsbqhSoqqj3YCk40PKDVs',
    'BASE_URL': 'https://web-stage.voxy.com/partner_api'
}

def get_authorization_header_for_post(data, api_key=CONFIG['API_KEY'], api_secret=CONFIG['API_SECRET']):
    url_encoded_data = urlencode(sorted(data.items()))
    hashed_data = sha256(api_secret + url_encoded_data)
    return {
        'AUTHORIZATION': 'Voxy %s:%s' % (api_key, hashed_data.hexdigest())
    }


def get_authorization_header_for_get(api_key=CONFIG['API_KEY'], api_secret=CONFIG['API_SECRET']):
    hashed_data = sha256(api_secret.encode('utf-8'))
    return {
        'AUTHORIZATION': 'Voxy %s:%s' % (api_key, hashed_data.hexdigest())
    }


def post(url, data=None, headers=None, **kwargs):
    if headers is None:
        headers = get_authorization_header_for_post(data)
    return requests.post(url, data=data, headers=headers, **kwargs)


def get(url, headers=None, **kwargs):
    if headers is None:
        headers = get_authorization_header_for_get()
    return requests.get(url, headers=headers, **kwargs)


def put(url, data=None, headers=None, **kwargs):
    if headers is None:
        headers = get_authorization_header_for_post(data)
    return requests.put(url, data=data, headers=headers, **kwargs)


def url_for(view, base_url=None, **kwargs):
    if base_url is None:
        base_url = CONFIG['BASE_URL']
    if view == 'user-detail':
        return base_url + '/partners/users/{euid}/'.format(**kwargs)
    elif view == 'user-list':
        return base_url + '/partners/users/'
    elif view == 'assessments-list':
        return base_url + '/partners/users/{euid}/assessments/'.format(**kwargs)
    elif view == 'auth-token':
        return base_url + '/partners/users/{euid}/auth_token'.format(**kwargs)
