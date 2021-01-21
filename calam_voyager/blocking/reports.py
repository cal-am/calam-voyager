import requests

from ..base import base


__all__ = [
    'pull_report'
]

def pull_report(s: requests.Session, report_name: str, **params: str) -> requests.Response:
    """Pull report by filename and pass parameters to URL."""

    return s.post(base.YARDI_REPORT_URL, params={
        'action': 'report',
        'select': f'reports/{report_name}',
        **params,
    })
