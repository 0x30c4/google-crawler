#!/usr/bin/env python3
import asyncio
from pyppeteer import launch

from html_parser import GooglePageParser


async def search_and_parse(search_query: str, limit: int) -> dict:
    """
    Opens a google search page in chromium and passes the data to
    GooglePageParser to parse the page html and find  the meta text,
    domains and related search results.

    Parameters:
        search_query (str)   : Search query to be parsed.
        limit        (int)   : Search the amount of domains to be parsed.

    Returns:
        search_result (dict) : Search result in a dict.
    """
    browser = await launch(
        {
            "args": [
                '--no-sandbox',
                '--single-process',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--no-zygote',
            ]
        },
        headless=True,
        executablePath="/usr/bin/chromium-browser"
    )

    page = await browser.newPage()
    await page.setViewport({"width": 1600, "height": 900})
    await page.goto(
        'https://google.com/search?q={}&hl=en'.
        format(search_query.replace(" ", "+")))
    # waiting for 4 seconds to load the page
    await page.waitFor(4000)

    # putting the google search page content to the raw_html.
    raw_html = await page.content()

    # creating a GooglePageParser object
    g_parser_obj = GooglePageParser(search_query, raw_html)

    # parsing the data and putting it into the data
    data = g_parser_obj.parse_page(limit)

    await browser.close()

    return data


if __name__ == "__main__":
    # this is just for debugging and testing
    asyncio.get_event_loop().run_until_complete(
        search_and_parse("haha this is a browser")
    )
