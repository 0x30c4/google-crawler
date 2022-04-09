#!/usr/bin/env python3
import os
import sys
import inspect
from requests import get
currentdir = os.path.dirname(
                    os.path.abspath(
                        inspect.getfile(
                            inspect.currentframe()
                        )
                    )
            )
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

os.chdir('../')

from html_parser import GooglePageParser

cookies = {
    'NID': '511=IeUiqlGy7NCVJmny5YdN6Sl797aKc2GE0wR5MYsx4c52t02BhBIG9nYKCUjKJy0NV6ApuTzz_PxGEgFabCaj86BknApP2HBmlhHIVvORFtTTxbYxPzGTgWHEhyDoYtKXgo3HUhfaCXwXonnZ6b981m96KBGSlg4MshCmrEN4rss',
    '1P_JAR': '2022-03-31-08',
    'AEC': 'AVQQ_LAnr7-03AgUxwRp2IUbSfM6Z8A2bIM20Sb-K4zi0ZyMzuMiUBl3Ww',
    'DV': 'g0ESniGU6X8vQL5Nu0W6IhepqfHy_VeMYpTpdNrE6QMAAAA',
    'ANID': 'AHWqTUlzd0j5LYSqgrdYjduKxWsVxlhJ1gc940WJudPwZRwFVf-LBFcv3iiud6xp',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; \
                    Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'text/html,application/\
                    xhtml+xml,application/xml;q=0.9,image/avif,image\
                    /webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


def req(q: str) -> str:
    q = q.strip().replace(" ", "+")
    proxies = {"http": "http://5.79.66.2:13080"}
    response = get(
        f"https://www.google.com/search?q={q}&spell=1&hl=en",
        cookies=cookies,
        headers=headers,
        proxies=proxies
    )

    print(response.text)
    return response.text


if __name__ == "__main__":
    q = "this is a test"
    resp = req(q)
    g_parser_obj = GooglePageParser(q, resp)
    data = g_parser_obj.parse_page()

    print(__import__("json").dumps(data, indent=4))
