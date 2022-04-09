#!/usr/bin/env python3
from redis import Redis
from typing import Union
from msgpack import packb, unpackb


class RedisCache:
    """ This fucntion will parse the google's search page and
    will return a dict with the top 10 ranking URL's and there
    domains, meta title, meta description, snippet questions
    and related searches

    ...

    Attributes
    ----------
    host: str
        The redis host domain or ip.
    port: int, optional
        The redis db port.
        Default is 6379.
    password: str, optional
        The redis db password. Default is an empty
        sting.
    db: int, optional
        Data parsed form the google search.
        Default is 0
    ttl: int, optional
        Time to Live or ttl is for the expiry time of the
        keys. Default is 3600 seconds
    logging: logging module
        Logging module for error logging
    redis_client: Redis
        The Redis instances object.

    Methods
    -------
    cache_parser_response(dict_data: dict) -> int:
        Caches the dict obj into the redis.
    check_cache(hash_name: str) -> Union[dict, bool]:
        Checks if the hash_name exists in the db. If
        exists then returns it or returns False.
    """

    def __init__(
        self, host: str,
        port: int = 6379,
        password: str = '',
        db: int = 0,
        ttl: int = 3600,
        logging=None
    ) -> None:
        """Constructs all the necessary attributes for the person object.

        Parameters
        ----------
        host: str
            The redis host domain or ip.
        port: int, optional
            The redis db port.
            Default is 6379.
        password: str, optional
            The redis db password. Default is an empty
            string.
        db: int, optional
            Data parsed form the google search.
            Default is 0
        ttl: int, optional
            Time to Live or ttl is for the expiry time of the
            keys. Default is 3600 seconds
        logging: logging module
            Logging module for error logging

       """

        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.ttl = ttl
        # creating a Redis object.
        self.redis_client = Redis(
                                host=self.host,
                                port=self.port,
                                password=self.password,
                                db=self.db
                            )
        self.logging = logging

    def cache_parser_response(self, dict_data: dict) -> int:
        """Caches the dict obj into the redis.
        Parameters.

        Parameters
        ----------
            dict_data: str
                The dict object which will be cached.

        Returns
        -------
            retc: int
                The return status of the setex query.
        """
        # striping the leading ant trailing spaces of
        # the search_query and making it lower case.
        search_query = dict_data["search_query"].lower().strip()
        try:
            # try to put the data into the db.
            # if it successes then return the
            # status code for setex.
            retc = self.redis_client.setex(
                search_query,
                self.ttl,
                packb(dict_data)
            )
            return retc
        except Exception as e:
            # check if self.logging is provided.
            # if so then log the errro or just raise
            # the error.
            if self.logging:
                self.logging.logging.error(str(e))
            raise e

    def check_cache(self, hash_name: str) -> Union[dict, bool]:
        """Checks if the hash_name exists in the db. If
        exists then returns it or returns False.

        Parameters
        ----------
            hash_name: str
                The dict object which will be cached.

        Returns
        -------
            data: dict, bool
                The value of the 'hash_name' or False if
                it doesn't exists.
        """
        try:
            # striping the leading ant trailing spaces of
            # the hash_name and making it lower case.
            hash_name = hash_name.lower().strip()

            # making a query to the redis db.
            data = self.redis_client.get(hash_name)

            # if anything was returned then uppack it
            # else return false.
            if data:
                data = unpackb(data)
            else:
                data = False
            return data
        except Exception as e:
            # check if self.logging is provided.
            # if so then log the errro or just raise
            # the error.
            if self.logging:
                self.logging.logging.error(str(e))
            raise e


def main():
    # this is for just debugging and testing.
    with open("./app/tests/demo-resp-data.json") as data:
        data = __import__("json").loads(data.read())
    redc_obj = RedisCache(host="localhost")

    data_new = redc_obj.check_cache(data["search_query"])
    if not data_new:
        redc_obj.cache_parser_response(data)

    print(data_new)


if __name__ == "__main__":
    main()
