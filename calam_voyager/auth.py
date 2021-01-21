import aiohttp
from bs4 import BeautifulSoup

from . import base


__all__ = [
    'login'
]

async def login(s: aiohttp.ClientSession, username: str, password: str, db: base.DatabaseKind = base.DatabaseKind.LIVE) -> aiohttp.ClientResponse:
    async with s.get(base.YARDI_LOGIN_URL) as response:
        soup = BeautifulSoup(await response.text(), 'html.parser')

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

    response = await s.post(base.YARDI_LOGIN_URL, data=data, allow_redirects=False)
    voyager_cookie = ';'.join((
        value for key, value in response.headers.items()
        if key.lower() == 'set-cookie'
    ))
    s._default_headers.add('Cookie', voyager_cookie)

    return response
