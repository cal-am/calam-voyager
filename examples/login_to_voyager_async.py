import asyncio
import os

import aiohttp
import calam_voyager
from dotenv import load_dotenv


async def main():
    """Login to voyager using credentials stored in environment variables."""
    
    load_dotenv()
    
    jar = aiohttp.CookieJar(quote_cookie=False)
    async with aiohttp.ClientSession(cookie_jar=jar) as s:
        await calam_voyager.login(s, os.environ['VOYAGER_USERNAME'], os.environ['VOYAGER_PASSWORD'])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
