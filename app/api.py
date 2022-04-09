#!/usr/bin/env python3
from uvicorn import run, logging
from fastapi import (
                     FastAPI,
                     Request,
                     status,
                     HTTPException,
)
from time import time
from configs.config import (
                            title,
                            version,
                            contact,
                            description,
                            tags_metadata,
                            LOG_INI,
                            PORT,
                            WORKERS,
                            HOST,
                            RELOAD,
                            REDIS_HOST,
                            REDIS_PORT,
                            CACHE_TTL,
                            API_ENDPOINT_URL
)

# importing the parser
from main import search_and_parse
from cache_redis import RedisCache


app = FastAPI(
                title=title,
                description=description,
                version=version,
                contact=contact,
                openapi_tags=tags_metadata,
                openapi_url="/{}/openapi.json".format(API_ENDPOINT_URL),
                docs_url="/{}/docs".format(API_ENDPOINT_URL)
             )

redis_cache_obj = RedisCache(
                        host=REDIS_HOST,
                        port=REDIS_PORT,
                        logging=logging,
                        ttl=CACHE_TTL
                    )


@app.middleware("http")
async def add_process_time_header(
    request: Request, call_next
):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/{}".format(API_ENDPOINT_URL), tags=["Google Crawler"])
async def crawl_google(
    search_query: str,
    limit: int = 10
) -> dict:
    """
    This API-End Point parses the google search reseult and returns
    a JSON response with the meta text, domains and related search results.

    - **search_query** : Search query to be parsed.
    - **limit**        : Search the amount of domains to be parsed.
    """
    try:
        search_result = redis_cache_obj.check_cache(search_query)
        if not search_result:
            search_result = await search_and_parse(search_query, limit)
            redis_cache_obj.cache_parser_response(search_result)

    except Exception as e:
        logging.logging.error(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Internal Server Error!")
    return search_result


if __name__ == "__main__":
    run(
        "api:app", host=HOST, port=PORT,
        workers=WORKERS, reload=RELOAD, log_config=LOG_INI
    )
