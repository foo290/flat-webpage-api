import requests
from typing import Union
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self._tags = [
            'h1', 'h2', 'h3', 'h4', 'h4', 'h5', 'p', 'a'
        ]
        self._parser = BeautifulSoup
        self._result_dict = {}

    def include_tags(self, tags: list) -> bool:
        self._tags.extend(tags)
        return True

    def exclude_tags(self, tags: list) -> bool:
        for tag in tags:
            if tag in self._tags:
                self._tags.remove(tag)
            else:
                print(f'Tag {tag} was not in _tags')
        return True

    def get_results(self) -> Union[dict, bool]:
        return self._result_dict if self._result_dict else None

    @staticmethod
    def __parser_a(snippet) -> dict:
        return {snippet.string.strip(): snippet.get('href')}

    @staticmethod
    def __get_html(response: requests.Response) -> str:
        return response.text

    @staticmethod
    def __get_response(url: str) -> requests.Response:
        return requests.get(url)

    def __get_soup(self, html: str) -> BeautifulSoup:
        return self._parser(html, "lxml")

    def __parse_tags(self, soup: BeautifulSoup) -> None:
        self._result_dict = {'title': soup.title.string}
        for tag in self._tags:
            self._result_dict[tag] = []
            for found in soup.find_all(tag):
                if found and found.string:
                    if tag == "a":
                        self._result_dict[tag].append(self.__parser_a(found))
                    else:
                        self._result_dict[tag].append(found.string.strip())

    def run_parser(self, url: str) -> bool:
        response = self.__get_response(url)
        if response.status_code == 200:
            html = self.__get_html(response)
            soup = self.__get_soup(html)
            self.__parse_tags(soup)
            return True
        else:
            print(f'Status code was : {response.status_code}')
            return False


if __name__ == '__main__':
    obj = Scraper()
    obj.run_parser('https://www.github.com')
    print(obj.get_results())
