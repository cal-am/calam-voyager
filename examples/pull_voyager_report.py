import asyncio
import os
from datetime import date, timedelta

import aiohttp
import calam_voyager
import pandas as pd
from dotenv import load_dotenv


async def main():
    """Pull activities from the last week."""

    load_dotenv()

    today = date.today().strftime('%m/%d/%Y')
    seven_days_ago = (date.today() - timedelta(days=7)).strftime('%m/%d/%Y')

    jar = aiohttp.CookieJar(quote_cookie=False)
    async with aiohttp.ClientSession(cookie_jar=jar) as s:
        await calam_voyager.login(s, os.environ['VOYAGER_USERNAME'], os.environ['VOYAGER_PASSWORD'])
        response = await calam_voyager.pull_report(
            s, 'rs_CalAm_CRM_Pull_Activity.txt',
            dtfrom=seven_days_ago,
            dtto=today
        )
        html = await response.text()
        
    # convert html table to `pandas.DataFrame`
    df = pd.read_html(html)[0]
    df.columns = df.iloc[2]
    df = df.iloc[3:-1]
    df.reset_index(inplace=True, drop=True)
    df.rename_axis(None, axis=1, inplace=True)
    print(df.head())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
