import asyncio
import os
from unittest import TestCase as BaseTestCase

import aiohttp
import requests
from bs4 import BeautifulSoup
from calam_voyager.auth import login as async_login
from calam_voyager.blocking.auth import login as blocking_login
from calam_voyager.utils import async_test, test_requires
from dotenv import load_dotenv


class AsyncTests(BaseTestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.username = os.getenv('VOYAGER_USERNAME')
        self.password = os.getenv('VOYAGER_PASSWORD')
        
        async def setUp_inner(self):
            jar = aiohttp.CookieJar(quote_cookie=False)
            self.client = aiohttp.ClientSession(cookie_jar=jar)
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(setUp_inner(self))

    @async_test
    @test_requires('username', 'password')
    async def test_login(self):
        async with self.client:
            await async_login(self.client, self.username, self.password)
            async with self.client.get('https://www.yardiaspla2.com/04030calam/pages/menu.aspx') as response:
                soup = BeautifulSoup(await response.text(), 'html.parser')
            
            title = soup.find('title')
            self.assertIsNotNone(title)
            self.assertEqual(title.text.strip(), 'Yardi Systems, Inc. Voyager')

    def tearDown(self) -> None:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.client.close())


class BlockingTests(BaseTestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.username = os.getenv('VOYAGER_USERNAME')
        self.password = os.getenv('VOYAGER_PASSWORD')
        self.client = requests.Session()

    @test_requires('username', 'password')
    def test_login(self):
        response = blocking_login(self.client, self.username, self.password)
        self.assertEqual(response.url, 'https://www.yardiaspla2.com/04030calam/pages/menu.aspx')

    def tearDown(self) -> None:
        self.client.close()
