import aiohttp

from . import base


__all__ = [
    'pull_report'
]

async def pull_report(s: aiohttp.ClientSession, report_name: str, **params: str) -> aiohttp.ClientResponse:
    """Pull report by filename and pass parameters to URL."""

    return await s.post(base.YARDI_REPORT_URL, params={
        'action': 'report',
        'select': f'reports/{report_name}',
        **params,
    })
