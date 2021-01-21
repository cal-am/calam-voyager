import asyncio
from enum import Enum, auto


class DatabaseKind(Enum):
    LIVE = auto()
    TEST  = auto()

YARDI_LOGIN_URL = 'https://www.yardiaspla2.com/04030calam/pages/LoginAdvanced.aspx'
YARDI_REPORT_URL = 'https://www.yardiaspla2.com/04030calam/pages/SysSqlScript.aspx'