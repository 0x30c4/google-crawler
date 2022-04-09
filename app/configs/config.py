
from os import environ as env

title = "Google Crawler API"
LOG_INI = env["CONT_LOG_INI"]
version = env["VERSION"]
contact = {
        "name": "Sanaf",
        "email": "sanaf@0x30c4.dev",
    }
API_ENDPOINT_URL = env["APP_API_ENDPOINT_URL"]
description = """
This api will parse and organize the search results from google.
In the backend the the API usage pyppeteer in a docker container
to parse the google search result.
"""

crawler_doc = """
This API-End Point parses the google search reseult and returns
a JSON response with the meta text, domains and related search results.
""".replace("\n", "")

tags_metadata = [
    {
        "name": "Google Crawler",
        "description": crawler_doc
    },
]


# API host, port, etc configs.
HOST = env["HOST"]
PORT = int(env["PORT"])
WORKERS = int(env["WORKERS"])
RELOAD = int(env["RELOAD"])

REDIS_HOST = env["REDIS_SRV_DOMAIN"]
REDIS_PORT = env["REDIS_PORT"]
CACHE_TTL = int(env["REDIS_CACHE_TTL"])
