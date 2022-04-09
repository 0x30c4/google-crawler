from bs4 import BeautifulSoup as bs4


class GooglePageParser:
    """ This fucntion will parse the google's search page and
    will return a dict with the top 10 ranking URL's and there
    domains, meta title, meta description, snippet questions
    and related searches

    ...

    Attributes
    ----------
    search_query : str
        Search query to be parsed.
    raw_html : str
        The raw html parsed which will be parsed.
    parsed_data : dict
        Data parsed form the google search

    Methods
    -------
    parse_page(search_query: str, raw_html: str) -> dict:
        Parses the google search page.
    """
    def __init__(self, search_query: str, raw_html: str):
        """
        Constructs all the necessary attributes for the
        GooglePageParser object.

        Parameters
        ----------
            search_query : str
                Search query to be parsed.
            raw_html : str
                The raw html parsed which will be parsed.
        """
        self.raw_html: str = raw_html
        self.parser_type: str = "html.parser"
        self.soup: bs4 = bs4(self.raw_html, self.parser_type)
        self.parsed_data: dict = {}
        self.search_query = search_query

    def parse_page(self, limit: int = 10) -> dict:
        """
        Parses the google search page. And if 'limit' is passed then
        it will limit the search results within the 'limit'.

        Parameters
        ----------
            limit : str, optional
                The max amount of urls which will be parsed.
                By default it's 10.

        Returns
        -------
            dict : dict
                The top 10 urls with domain name, meta title, meta
                description, snippet questions and related,
                searches in a dict.
        """

        results = {
            "search_query": self.search_query,
            "domains": [],
            "people_also_search_for": []
        }

        n = 0

        # finding the related search.
        # all the related search elements has a div after
        # and before them not td and span.
        for a in self.soup.find_all("a"):
            a_href = a.get("href")
            # 1st check if the link has /search at the beginning
            # if there is then check check if it has td as parent
            # because the next page numbers has td as parent.
            # then check if the children of it has span because
            # the other pages at the top like videos, images, all,
            # etc has span as children. also exclude the a tags that
            # has span as there parent. and if the length of the text in
            # a tag is greater than the search_query then append the
            # results.
            try:
                if a_href and a_href.startswith("/search") \
                        and a.parent.name != "td" \
                        and a.children.__next__().name != "span" \
                        and a.parent.name != "span" \
                        and a.get_text().__len__() \
                        >= self.search_query.__len__():

                    # if related results has the search_query in it
                    if self.search_query.split(" ")[0].lower() in a.get_text():
                        results["people_also_search_for"].append(a.get_text())
            except StopIteration:
                # a.children is a list_iterator obj
                # and if it hits StopIteration then
                # break the loop
                break

        # removing the 1st element of people_also_search_for because
        # this the "people also search for" text
        if results["people_also_search_for"].__len__() > 1:
            results["people_also_search_for"].pop(0)

        # reinitalizing soup object
        self.soup: bs4 = bs4(self.raw_html, self.parser_type)

        for h3 in self.soup.find_all("h3"):

            # Go through all the h3 tags and parse the
            # title, link, meta text and etc.
            h3_title = h3.text  # get the title
            link_href = h3.parent.get("href")  # get the link of the title

            # Getting all the span's because the meta text is contained in
            # a span.
            spans = h3.parent.parent.parent.parent.find_all("span")

            # Go through all the span while checking if the parent of
            # the span is a div if so, then we've found the meta text.
            # also check of there's any meta_text text related to the link.
            if spans.__len__() > 1:
                meta_text = spans[-1].get_text()

            if meta_text == "":
                for span in spans:
                    if span.get_text().__len__() > 15:
                        meta_text = span.get_text()
                    # print(span.get_text().__len__(), span, sep=" | ")

            if link_href is not None:
                results["domains"].append(
                    {
                        "title": h3_title,
                        "link": link_href,
                        "meta_text": meta_text,
                    }
                )
                # break if the limit is hited.
                if n == limit:
                    break
                n += 1

        # print(__import__("json").dumps(results, indent=4))
        return results


if __name__ == "__main__":
    with open("./tests/search_page_2.html", encoding="utf-8") as raw_html:
        raw_html = raw_html.read()

    g_parser = GooglePageParser(raw_html)

    results = g_parser.parse_page(100)
    print(results)
