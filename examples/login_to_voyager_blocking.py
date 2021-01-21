import calam_voyager.blocking
import requests
import os
from dotenv import load_dotenv


def main():
    """Login to voyager using credentials stored in environment variables."""

    load_dotenv()

    with requests.session() as s:
        calam_voyager.blocking.login(s, os.environ['VOYAGER_USERNAME'], os.environ['VOYAGER_PASSWORD'])


if __name__ == "__main__":
    main()