import typing
import httpx
from lxml import etree


class Response:
    def __init__(self, resp: httpx.Response) -> None:
        self._resp = resp
        if isinstance(self._resp, httpx.Response):
            self._dom = etree.HTML(self.text)
        else:
            raise TypeError(f"resp must be Response.")

    def json(self) -> typing.Any:
        return self._resp.json()

    @property
    def url(self) -> str:
        return self._resp.url

    @property
    def text(self) -> str:
        return self._resp.text

    def xpath(self, xpath: str):
        if isinstance(xpath, str):
            return self._dom.xpath(xpath)
        else:
            raise TypeError(f"xpath must be Response.")
