import requests
from bs4 import BeautifulSoup

from .. import base


__all__ = [
    'login'
]

def login(s: requests.Session, username: str, password: str, db: base.DatabaseKind = base.DatabaseKind.LIVE) -> requests.Response:
    response = s.get(base.YARDI_LOGIN_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    inputs = soup.select('form input')
    data = {
        el['name']: el['value']
        for el in inputs
        if el.get('name') and el.get('value')
    }
    data.update({
        'Username': username,
        'Password': password,
        'Destination': db.name.title()
    })

    return s.post(base.YARDI_LOGIN_URL, data=data)